import streamlit as st
from datetime import date
import random

# Page Configuration
st.set_page_config(page_title="Palavra do Dia", page_icon="🇵🇹", layout="centered")

# A1 Portuguese Vocabulary Database
# In a larger app, this could be loaded from a JSON file or a database.
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
        "word": "Obrigado / Obrigada",
        "translation": "Thank you (masculine / feminine)",
        "pronunciation": "oh-bree-GAH-doo / dah",
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

# Generate the Daily Word
today = date.today()
# Seed the random choice with today's date so it stays the same all day
random.seed(today.toordinal())
daily_word = random.choice(a1_words)

# UI Layout
st.title("🇵🇹 Palavra do Dia")
st.markdown("### Your Daily A1 Portuguese Word")
st.divider()

# Word Display
st.header(daily_word["word"])
st.caption(f"Part of Speech: {daily_word['type']}")

st.markdown(f"**Translation:** {daily_word['translation']}")
st.markdown(f"**Pronunciation:** *{daily_word['pronunciation']}*")

st.info(f"**Example Sentence:** {daily_word['example']}")

st.divider()
st.write(f"📅 *Word for {today.strftime('%B %d, %Y')}*")