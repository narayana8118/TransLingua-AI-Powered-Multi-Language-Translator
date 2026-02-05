import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Configure API key
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key="AIzaSyCaWFR0fKLt2BWGq5tEopsgDruNIbPHzbs")


# Initialize Model
model = genai.GenerativeModel("models/gemini-flash-latest")




# Translation Function
def translate_text(text, source_language, target_language):

    prompt = f"""
    Translate the following text from {source_language}
    to {target_language}:

    {text}
    """

    response = model.generate_content(prompt)

    return response.text


# Main App
def main():

    # Page Config
    st.set_page_config(
        page_title="AI-Powered Language Translator",
        page_icon="🌐"
    )

    # Header
    st.header("🌐 AI-Powered Language Translator")

    # Text Input
    text = st.text_area("✍️ Enter text to translate:")

    # Language Selection
    source_language = st.selectbox(
        "🌍 Select source language:",
        ["English", "Spanish", "French", "German", "Chinese", "Telugu", "Hindi"]
    )

    target_language = st.selectbox(
        "🌎 Select target language:",
        ["English", "Spanish", "French", "German", "Chinese", "Telugu", "Hindi"]
    )

    # Translate Button
    if st.button("🔁 Translate"):

        if text and source_language and target_language:

            try:

                translated_text = translate_text(
                    text,
                    source_language,
                    target_language
                )

                st.subheader("📝 Translated Text:")
                st.write(translated_text)

            except Exception as e:

                st.error(f"⚠️ Error: {str(e)}")

        else:
            st.warning("⚠️ Please fill in all fields.")


# Run App
if __name__ == "__main__":
    main()
