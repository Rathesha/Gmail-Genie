import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyCS0C8fmXwf6k8b4Mi5ZPiIHyqJDaSGqKk")

# Custom Styling
st.markdown(
    """
    <style>
        .centered {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #333333;
            margin-top: 10px;
        }
        .subtitle {
            font-size: 18px;
            color: #666666;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display Logo and Title in Center
st.markdown('<div class="centered">', unsafe_allow_html=True)
# st.image("logo.jpg", width=120)
st.markdown('<div class="title">🤖 Gmail Genie Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Effortlessly manage your emails with AI ✨</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Add Some Space
st.write("\n\n")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    # Append user input to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generate response from Gemini API
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)
    bot_response = response.text if response else "Sorry, I couldn't process that."
    
    # Append bot response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": bot_response})
    
    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)
