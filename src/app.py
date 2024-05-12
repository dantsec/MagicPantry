#
# Try to import necessary packages.
#
try:
    # Web runner.
    import streamlit as st
    # Google Gemini AI.
    import google.generativeai as genai
    # Lib's to load environment variables.
    from os import getenv
    from dotenv import load_dotenv
    # Sleep to avoid web-service errors (ResourceExhausted, google.api_core.exceptions.ResourceExhausted).
    from time import sleep
    # Model config variables.
    from utils.model_config import *
except ModuleNotFoundError:
    raise Exception("Failed to import packages!")


#
# Load Google Gemini principal variables.
#
def load_gemini() -> None:
    load_dotenv(override=True)
    genai.configure(api_key=getenv("GOOGLE_GEMINI_API_KEY"))


#
# Set up the model.
#
def setup_model() -> genai.GenerativeModel:
    return genai.GenerativeModel(
        model_name=MODEL_NAME,
        generation_config=GENERATION_CONFIG,
        safety_settings=SAFETY_SETTINGS,
        system_instruction=SYSTEM_INSTRUCTION,
    )


#
# Setup page config.
#
def load_steamlit_header() -> None:
    st.set_page_config(
        page_title="Magic Pantry @ Gemini AI Project",
        page_icon="🍳",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    st.markdown('### Hello, I\'m Magic Pantry! 👋')
    st.markdown('- When you have a list of ingredients but no idea what recipes you can make, call me! 🤖')
    st.markdown('- Find more information about me and my creator by clicking [**here**](https://github.com/dantsec/MagicPantry)!')

    st.divider()


#
# Return the chatbot text icon type (user or model).
#
def role_to_streamlit(role):
  if role == "model":
    return "assistant"
  else:
    return role


#
# Setup streamlit.
#
def main() -> None:
    load_gemini()
    model = setup_model()

    # Add a Gemini Chat history object to Streamlit session state.
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history=HISTORY)

    # Page setup.    
    load_steamlit_header()

    # For init, show just bot instructions message.
    for message in st.session_state.chat.history:
        if "Vamos pensar passo a passo." not in message.parts[0].text:
            with st.chat_message(role_to_streamlit(message.role)):
                st.markdown(message.parts[0].text)

    # Accept user's next message, add to context, resubmit context to Gemini and show the received response.
    if prompt := st.chat_input("What ingredients do you have now?"):
        st.chat_message("user").markdown(prompt)

        response = st.session_state.chat.send_message(prompt)
        sleep(3)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)


#
# Here, the magic happens!
#
if __name__ == "__main__":
    main()
