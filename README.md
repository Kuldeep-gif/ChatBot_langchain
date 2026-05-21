# 🤖 AI Chatbot with Groq + LangChain + Streamlit

An AI chatbot built using **Groq, LangChain, LangGraph, Streamlit, and
Google Serper Search API**.

The chatbot supports:

-   Conversational AI interactions
-   Google web search integration
-   Session-based chat history
-   Memory handling
-   Chat-style Streamlit interface
-   Typing animation effect

## 🚀 Tech Stack

-   Python
-   Groq
-   LangChain
-   LangGraph
-   Streamlit
-   Google Serper API
-   python-dotenv

## 📂 Project Structure


    AI-Chatbot/
    │
    ├── app.py
    ├── .env
    ├── requirements.txt
    ├── README.md   
    └── .gitignore

## ⚙️ Installation

Clone the repository:

``` bash
git clone <your-repo-url>
cd AI-Chatbot
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Create a `.env` file:

``` env
GROQ_API_KEY=your_key
SERPER_API_KEY=your_key
```

Run the application:

``` bash
streamlit run app.py
```

## ✨ Features

-   AI-powered chatbot
-   Google search tool integration
-   Persistent conversation history
-   Interactive chat UI
-   Typing effect simulation

## 🔧 Challenges Faced

During development:

-   Tool-calling failures with Groq
-   Streaming vs invoke behavior
-   Session state handling
-   LangChain compatibility issues
-   Memory management conflicts

## 📚 Learnings

Building AI applications is not only about prompting models.

Major learning areas:

-   Tool calling
-   API integration
-   Session state management
-   Agent workflows
-   Debugging AI systems

## 📄 License

Open-source for learning and educational purposes.
