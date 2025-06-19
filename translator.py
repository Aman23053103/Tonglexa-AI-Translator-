import streamlit as st
import google.generativeai as genai

# ----------------------------
# Configure Gemini API Key
# ----------------------------
GOOGLE_API_KEY = "YOUR API KEY"  # ← Replace with your actual Gemini API key
genai.configure(api_key=GOOGLE_API_KEY)

# Use Gemini Flash (optimized for speed)
model = genai.GenerativeModel("gemini-1.5-flash")

# ----------------------------
# Language Map (Add more if needed)
# ----------------------------
LANGUAGE_MAP = {
    "English": "English",
    "Hindi": "Hindi",
    "French": "French",
    "German": "German",
    "Spanish": "Spanish",
    "Italian": "Italian",
    "Russian": "Russian",
    "Chinese (Simplified)": "Chinese",
    "Arabic": "Arabic",
    "Bengali": "Bengali",
    "Tamil": "Tamil",
    "Telugu": "Telugu",
    "Urdu": "Urdu"
}

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="🌍 Tonglexa (AI Translator)", layout="centered")
st.title("🌍 Tonglexa (AI Translator)")
st.markdown("🔤 Translate text using **Tonglexa**")

# Language Selection
source_lang = st.selectbox("Translate From", list(LANGUAGE_MAP.keys()), index=0)
target_lang = st.selectbox("Translate To", list(LANGUAGE_MAP.keys()), index=1)
input_text = st.text_area("Enter text to translate", height=150)

# Translate Button
if st.button("Translate"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text.")
    elif source_lang == target_lang:
        st.info("ℹ️ Source and target languages are the same.")
        st.write(input_text)
    else:
        try:
            # Tonglexa translation prompt
            prompt = f"""You are Tonglexa, a professional multilingual AI translator. Translate the following text from {source_lang} to {target_lang} with high accuracy and cultural context.
            Text: \"{input_text}\""""

            response = model.generate_content(prompt)
            output = response.text.strip()

            st.success(f"Translated ({target_lang}):")
            st.write(output)

        except Exception as e:
            st.error(f"⚠️ Translation Error: {e}")
