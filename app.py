import streamlit as st
import joblib

model = joblib.load('models/spam_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

st.title("Spam Email Classifier")
user_input = st.text_area("Paste your email or SMS text here:")

if st.button("Predict"):
    user_input_vec = vectorizer.transform([user_input])
    pred = model.predict(user_input_vec)[0]
    st.write("Prediction:", "🚫 Spam" if pred == 1 else "✅ Not Spam")
