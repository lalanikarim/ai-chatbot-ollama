---
title: Ai Chatbot w/ Langchain, Ollama, and Streamlit
emoji: 📊
colorFrom: indigo
colorTo: gray
sdk: streamlit
sdk_version: 1.28.0
app_file: main.py
pinned: false
license: mit
---

# Streamlit + Langchain + Ollama w/ Mistral

Run your own AI Chatbot locally on a GPU or even a CPU.

To make that possible, we use the [Mistral 7b](https://mistral.ai/news/announcing-mistral-7b/) model.  
However, you can use any quantized model that is supported by [llama.cpp](https://github.com/ggerganov/llama.cpp).

This AI chatbot will allow you to define its personality and respond to the questions accordingly.  
There is no chat memory in this iteration, so you won't be able to ask follow-up questions.
The chatbot will essentially behave like a Question/Answer bot.

# TL;DR instructions

1. Install ollama
2. Install langchain
3. Install streamlit
4. Run streamlit

# Step by Step instructions

The setup assumes you have `python` already installed and `venv` module available.

1. Install `ollama` from [ollama.ai](https://ollama.ai).
2. Download `mistral` llm using `ollama`:
```bash
ollama pull mistral
```
3. Download the code or clone the repository.
4. Inside the root folder of the repository, initialize a python virtual environment:
```bash
python -m venv .venv
```
5. Activate the python environment:
```bash
source .venv/bin/activate
```
6. Install required packages (`langchain` and `streamlit`):
```bash
pip install -r requirements.txt
```
7. Start `streamlit`:
```bash
streamlit run main.py
```

