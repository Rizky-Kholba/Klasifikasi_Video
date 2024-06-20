import streamlit as st
from helper.download import *
from helper.transcribe import *


st.set_page_config(
    page_title="Klasifikasi Topik Video",
    page_icon="🎥",
    initial_sidebar_state="expanded",
)

st.title("Video Clasification")

source = st.selectbox(
    "Pilih Source Video", ["YouTube", "Upload dari penyimpanan lokal"]
)

if source == "YouTube":
    url = st.text_input("Masukkan URL YouTube")
    if url:
        # tampilkan dan download video
        st.video(url)
        with st.spinner("Downloading..."):
            title = yt_downloader(url)
        st.subheader(f"Judul video: {title}")

        # proses traskrip
        placeholder = st.empty()
        if placeholder.button("Mulai Proses"):
            title = title + ".mp4"
            label, text = yt_clasify_pipeline(title)
            placeholder.empty()
            st.success(f"{label}")
            # st.write(f"Transcribed Text: {text}")

elif source == "Upload dari penyimpanan lokal":
    uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov", "mkv"])
    if uploaded_file is not None:
        with st.spinner("Downloading..."):
            up_video, vid_name = save_uploaded_file(uploaded_file)

        # tampilkan dan download video
        st.video(up_video)
        title = vid_name
        st.subheader(f"{title}")
        st.subheader(f"{up_video}")

        # proses traskrip
        placeholder = st.empty()
        if placeholder.button("Mulai Proses"):
            label, text = yt_clasify_pipeline(title)
            placeholder.empty()
            st.success(f"Prediksi Topik: {label}")
            # st.write(f"Transcribed Text: {text}")
