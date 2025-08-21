import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage 

def get_response(user_input):
    return "I Don't Know"

# App Config
st.set_page_config(page_title="Ask a Question", page_icon="🤖")
st.title("Ask a Question")

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello, I am a bot. How can I help you?"),
    ]

# Side Bar
with st.sidebar:
    st.header("Settings")
      # Make website URL fixed
    website_url = st.text_input(
        "Website URL",
        value="https://atdigital.io/",  
        disabled=True # Makes it read-only
    )

# User Input
user_query = st.chat_input("Type your message here...")

if user_query is not None and user_query != "":

    response = get_response(user_query)

    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=response))

 # conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)    

