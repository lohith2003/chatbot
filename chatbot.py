import streamlit as st

st.title("spider")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Displaying the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to input
prompt = st.chat_input("Type your message here...")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Simple response logic
    response = ""
    if "hello" in prompt.lower():
        response = "Hi there! How can I help you today?"
    elif "hi" in prompt.lower():
        response="hi how's is your day 😊"
    elif "help me with aadharcard" in prompt.lower():
        response="hi how's"
    elif "bye" in prompt.lower():
        response = "Goodbye! Have a great day!"
    else:
        response = "I didn't understand that. Can you please rephrase?"

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
