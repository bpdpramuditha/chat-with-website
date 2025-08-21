import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage 
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_response(user_input):
    return "I Don't Know"

def get_vectorstore_from_url(url):
    # get the text in document form
    data_loader = WebBaseLoader(url)
    document = data_loader.load()

     # split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_parts = text_splitter.split_documents(document)
    return document_parts

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

document_parts = get_vectorstore_from_url(website_url)
with st.sidebar:
    st.write(document_parts)

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

