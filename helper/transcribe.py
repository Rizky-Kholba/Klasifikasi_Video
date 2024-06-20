import pandas as pd
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import whisper
import warnings
import pickle
import streamlit as st


# Cleaning
def cleaning_text(text):
    text = text.lower()  # lower case
    text = re.sub(r"http?://\S+|www\.\S+", "", text)  # hapus URL
    text = re.sub(r"[-+]?[0-9]", "", text)  # hapus angka
    text = re.sub(r"[^\w\s]", "", text)  # hapus simbol/tanda baca
    text = text.strip()  # hapus whitespace

    return text


# Lemmatization
key_norm = pd.read_csv(".\corpus\key_norm.csv")


def lematization(text):
    text = " ".join(
        [
            (
                key_norm[key_norm["singkat"] == word]["hasil"].values[0]
                if (key_norm["singkat"] == word).any()
                else word
            )
            for word in text.split()
        ]
    )

    text = str.lower(text)
    return text


# Stemming
factory = StemmerFactory()
steammer = factory.create_stemmer()


def stemming(text):
    text = steammer.stem(text)
    return text


# Stopword Removal
nltk.download("stopwords")
stopwords_ind = stopwords.words("indonesian")

more_stopword = [
    "ya",
    "terima",
    "kasih",
    "tidak",
    "tonton",
    "selamat",
    "pagi",
    "siang",
    "sore",
    "malam",
    "kanal",
    "like",
    "share",
    "cahnnel",
    "langganan",
    "video",
    "buka",
    "kemaks",
    "guna",
    "lihat",
]  # adding word
stopwords_ind = stopwords_ind + more_stopword


def stopwords_removal(text):
    clean_word = []
    text = text.split()
    for word in text:
        if word not in stopwords_ind:
            clean_word.append(word)

    return " ".join(clean_word)


# Pipeline Preprocessing
def text_preprocessing_pipeline(text):
    text = cleaning_text(text)
    text = lematization(text)
    text = stopwords_removal(text)
    text = stemming(text)
    return text


# Transcribe
def transcribe_audio(title):

    warnings.filterwarnings("ignore")
    model = whisper.load_model("base")
    result = model.transcribe(f"downloads/{title}", language="id")

    return result["text"]


# Predict
with open("svm_model.pkl", "rb") as file:
    svm_model = pickle.load(file)


def yt_clasify_pipeline(title):
    with st.spinner("Transcribing..."):
        text = transcribe_audio(title)

    with st.spinner("Preprocessing..."):
        text = text_preprocessing_pipeline(text)

    with st.spinner("Predicting..."):
        predicted_label = svm_model.predict([text])

    return predicted_label[0], text
