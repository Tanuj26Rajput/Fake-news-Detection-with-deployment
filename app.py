import streamlit as st
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

model = load_model("fake_news_classifier_model.h5")
with open("tokenizer.pkl", "rb") as file:   
    tokenizer = pickle.load(file)

def predict_fake_news(title, text):
    content = title + " " + text
    sequences = tokenizer.texts_to_sequences([content])
    padded_sequences = pad_sequences(sequences, maxlen=500, padding='post', truncating='post')
    prediction = model.predict(padded_sequences)[0][0]
    return "Real News" if prediction > 0.5 else "Fake News"

st.set_page_config(page_title="Fake News Detection", page_icon="📰")
st.title("📰 Fake News Classifier (LSTM)")
st.markdown("Build using LSTM and TensorFlow")

title = st.text_input("Enter the news title:")
text = st.text_area("Enter the news content:")

if st.button("Predict"):
    if title.strip() == "" or text.strip() == "":
        st.warning("Please enter both title and content to make a prediction.")
    else:
        result = predict_fake_news(title, text)
        st.success(f"The news is classified as: **{result}**")
        st.balloons()