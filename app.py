import streamlit as st
from datetime import date
import random
from gtts import gTTS
import io

# Page Configuration
st.set_page_config(page_title="Palavra do Dia", page_icon="🇵🇹", layout="centered")

# A1 Portuguese Vocabulary Database
a1_words = [
    {
        "word": "Bom dia",
        "translation": "Good morning",
        "pronunciation": "bohm DEE-ah",
        "example": "Bom dia! Como você está?",
        "type": "Greeting"
    },
    {
        "word": "Água",
        "translation": "Water",
        "pronunciation": "AH-gwah",
        "example": "Eu gostaria de uma água, por favor.",
        "type": "Noun"
    },
    {
        "word": "Comer",
        "translation": "To eat",
        "pronunciation": "koh-MEHR",
        "example": "Eu gosto de comer pão.",
        "type": "Verb"
    },
    {
        "word": "Obrigado",
        "translation": "Thank you (masculine)",
        "pronunciation": "oh-bree-GAH-doo",
        "example": "Muito obrigado pela ajuda.",
        "type": "Expression"
    },
    {
        "word": "Sempre",
        "translation": "Always",
        "pronunciation": "SEHM-pree",
        "example": "Ela sempre estuda de manhã.",
        "type": "Adverb"
    }
]

# Function to generate Portuguese audio on the fly
def get_audio(text):
    tts = gTTS(text=text, lang='pt')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp

# Generate the Daily Word
today = date.today()
random.seed(today.toordinal())
daily_word = random.choice(a1_words)

# UI Layout
st.title("🇵🇹 Palavra do Dia")
st.markdown("### Your Daily A1 Portuguese Word")
st.divider()

# Word Display
st.header(daily_word["word"])
st.caption(f"Part of Speech: {daily_word['type']}")

# Add the Audio Player right under the word
audio_data = get_audio(daily_word["word"])
st.audio(audio_data, format="audio/mp3")

st.divider()

# --- THE ENIGMA PUZZLE ---
st.markdown("### 🕵️ Decipher the Word")
st.write("Test your memory before revealing the answer.")

# 1. The Guessing Input
user_guess = st.text_input("Enter the English translation:", placeholder="Type your guess here...")

# Clean up the true translation for comparison (removes things like "(masculine)")
target_translation = daily_word['translation'].lower().split(' (')[0]

if user_guess:
    if user_guess.lower().strip() == target_translation:
        st.success("Correct! You cracked it. 🎉")
        st.balloons()
    else:
        st.error("Not quite! Try again or unlock the answer below.")

# 2. The Reveal Expander
with st.expander("🗝️ Unlock Translation & Context"):
    st.markdown(f"**Translation:** {daily_word['translation']}")
    st.markdown(f"**Pronunciation:** *{daily_word['pronunciation']}*")

    st.info(f"**Example Sentence:** {daily_word['example']}")

    # Audio for the example sentence
    st.write("Listen to context:")
    example_audio = get_audio(daily_word["example"])
    st.audio(example_audio, format="audio/mp3")

st.divider()
st.write(f"📅 *Word for {today.strftime('%B %d, %Y')}*")