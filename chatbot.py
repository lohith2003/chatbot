import streamlit as st

st.title("Gov Vault Chatbot")

# Initialize chat history and user session states
if "messages" not in st.session_state:
    st.session_state.messages = []
if "menu_mode" not in st.session_state:
    st.session_state.menu_mode = False  # False means not in menu mode yet
if "bot_active" not in st.session_state:
    st.session_state.bot_active = False  # False means bot is inactive

# Displaying the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Define government-related services responses
def handle_gov_services(option):
    if option == "1":
        return "You can apply for Aadhaar by having proof of identity, address, and age."
    elif option == "2":
        return "To apply for a passport, you'll need to fill out the application form, submit identification documents, and schedule an appointment at your nearest passport office."
    elif option == "3":
        return "For a PAN card, apply through the NSDL or UTIITSL website. Make sure to provide proof of identity and address."
    elif option == "4":
        return "You can apply for a Voter ID by visiting the National Voters' Service Portal (NVSP) and filling out Form 6."
    elif option == "5":
        return "To apply for a driving license, go to the RTO website, fill the application form, and submit the required documents."
    elif option == "6":
        return "You can check the status of your application on the respective official website of the service you applied for."
    else:
        return "Invalid option. Please enter a valid number (1-6)."

# Display the main menu to users
def display_menu():
    return (
        "Welcome to Gov Vault! Please choose a service:\n"
        "1. Aadhaar\n"
        "2. Passport\n"
        "3. PAN Card\n"
        "4. Voter ID\n"
        "5. Driving License\n"
        "6. Check Application Status"
    )

# React to input
prompt = st.chat_input("Type your message here...")

if prompt:
    # User input
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Check for "hi", "hello", and "bye" commands
    if prompt.lower() in ["hi", "hello"]:
        response = "Hi there! How can I assist you today? press any key to start the service"
        st.session_state.bot_active = True  # Activate bot services
        st.session_state.menu_mode = False  # Reset menu mode to show the menu
    elif prompt.lower() == "bye":
        response = "Goodbye! I am stopping services. Say 'hi' to start again."
        st.session_state.bot_active = False  # Deactivate bot services
    elif st.session_state.bot_active:
        # If the bot is active, proceed with normal service logic
        if not st.session_state.menu_mode:
            # First time user input, display the menu
            response = display_menu()
            st.session_state.menu_mode = True  # Set to True to expect numeric input next
        else:
            # Handle numeric input as service selection
            response = handle_gov_services(prompt)
            st.session_state.menu_mode = False  # Reset after a service is chosen
    else:
        # If bot is inactive (after saying "bye")
        response = "The bot is inactive. Please say 'hi' to restart the conversation."

    # Assistant response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
