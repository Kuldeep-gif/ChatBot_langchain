from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.tools import tool
import streamlit as st

llm = ChatGroq(model="llama-3.3-70b-versatile", streaming=True)

search = GoogleSerperAPIWrapper()

@tool
def google_search(query: str) -> str:
    """Search Google for recent information."""
    return search.run(query)

tools = [google_search]


if "memory" not in st.session_state:
    st.session_state.memory = MemorySaver()

if "history" not in st.session_state:
    st.session_state.history = []


agent = create_agent(
    model=llm,
    tools=tools,
    checkpointer=st.session_state.memory,
    system_prompt="You are an amazing AI agent who can search Google. Provide short and concise"
)
print(st.session_state.memory)

#### BUILDING WEB INTERFACE
st.subheader("🤖 Chat Bot - Ask me anything")

for messages in st.session_state.history:
    role = messages['role']
    content = messages['content']
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask Anything")

if query:
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role":"user","content":query})

    res = agent.stream(
        {"messages":[{"role":"user","content":query}]},
        {"configurable":{"thread_id":"1"}},
        stream_mode="messages"
    )

    ai_container = st.chat_message('assistant')
    with ai_container:
        space = st.empty()

        messages = ""

        for chunk in res:
            messages = messages+chunk[0].content
            space.write(messages)


    
        st.session_state.history.append(
    {"role":"assistant","content":messages}
)