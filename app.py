import streamlit as st

#app config
st.set_page_config(page_title="Ask a Question", page_icon="🤖")
st.title("Ask a Question")

# sidebar
with st.sidebar:
    st.header("Settings")
      # Make website URL fixed
    website_url = st.text_input(
        "Website URL",
        value="https://atdigital.io/",  
        disabled=True                  # makes it read-only
    )

# user input
user_query = st.chat_input("Type your message here...")

with st.chat_message("AI"):
    st.write("Hello, how can I help you?")