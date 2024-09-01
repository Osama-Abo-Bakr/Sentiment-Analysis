# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import streamlit as st
import pickle


model = pickle.load(open(r'D:\Pycharm\Computer Vision Project\NLP Project\Sentiment Analysis (English)\rf_model.bin', 'rb'))
tokenizer = pickle.load(open(r'D:\Pycharm\Computer Vision Project\NLP Project\Sentiment Analysis (English)\TFIDF.bin', 'rb'))
class_label = {1: 'Good', 0: 'Bad'}
st.title('Sentiment Analysis (English). 📰️')

text = st.text_input('Enter THe Text')
if text:
    text = tokenizer.transform([text])
    if st.button('predict'):
        prediction = model.predict(text)[0]
        st.write(class_label[prediction])
