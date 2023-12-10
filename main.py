from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOllama
from langchain.schema import HumanMessage, AIMessage
import urllib.request, json
import streamlit as st

@st.cache_resource
def get_ollama_models(ollama_server_url):
    api_tags = "/api/tags"
    models = []
    with urllib.request.urlopen(ollama_server_url + api_tags) as tags:
        response = json.load(tags)
        models = [model['name'] for model in response['models']]

        # This is not necessary but added here to keep the output clean
        models = [model.replace(":latest","") for model in models]
    return tuple(models)

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)

st.title("LangChain + Streamlit + Ollama")

with st.sidebar:
    # Url of the hosted ollama instance.
    ollama_server = st.text_input("Ollama API Server", value="http://localhost:11434")
    ollama_model = st.selectbox("Ollama model name", get_ollama_models(ollama_server), index=None)
    
    st.markdown("""
    Changing the model doesn't clear the history which gets passed to the new llm as context.  
    Use the below button to clear chat history and start with a clear slate.
    """)
    if st.button("Clear chat history", type="primary"):
        st.session_state["messages"] = [AIMessage(content="How can I help you?")]


if "messages" not in st.session_state:
    st.session_state["messages"] = [AIMessage(content="How can I help you?")]

for msg in st.session_state.messages:
    st.chat_message(msg.type).write(msg.content)

if prompt := st.chat_input():
    st.session_state.messages.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)

    if not ollama_model:
        st.info("""Please select an existing Ollama model name to continue.
        Visit https://ollama.ai/library for a list of supported models.
        Restart the streamlit app after downloading a model using the `ollama pull <model_name>` command.
        It should become available in the list of available models.""")
        st.stop()

    with st.chat_message("assistant"):
        stream_handler = StreamHandler(st.empty())
        llm = ChatOllama(model=ollama_model, streaming=True, callbacks=[stream_handler])
        response = llm(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))
