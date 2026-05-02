# 🧑‍💻⚡ Gaurav - Tech Chatbot (LangChain + Groq + Streamlit)

An AI-powered **tech chatbot** built using **LangChain, Groq LLM, and Streamlit**.  
It answers only technical questions and provides a clean chat interface.

##  Tech Stack

- Python 
- Streamlit 
- LangChain 
- Groq API 
- dotenv

## 📁 Project Structure

```
langchain-groq-streamlit-app/
│
├── app/
│   ├── chains.py        # LangChain pipeline
│   ├── llm.py           # Groq LLM setup
│   ├── prompts.py       # System prompt
│   ├── config.py        # API key & settings
│
├── app.py               # Streamlit entry point
├── .env                 # Environment variables
├── requirements.txt
├── README.md
```

**How to run Code:** 
```
-Create virtual environment :uv venv
-Install dependencies : pip install requirement.txt
-Add environment variables
  -GROQ_API_KEY=your_groq_api_key_here
  -MODEL_NAME=openai/gpt-oss-120b
- Run the application: streamlit run app.py
```
