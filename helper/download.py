import streamlit as st
from pytube import YouTube
import os
import shutil


DONWLOAD_FOLDER = "./downloads/"

# if not os.path.exists(DONWLOAD_FOLDER):
#    os.makedirs(DONWLOAD_FOLDER)


def delete_folder():
    if not os.path.exists(DONWLOAD_FOLDER):
        os.makedirs(DONWLOAD_FOLDER)

    for item_name in os.listdir(DONWLOAD_FOLDER):
        item_path = os.path.join(DONWLOAD_FOLDER, item_name)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.unlink(item_path)  # Menghapus file atau symlink
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)  # Menghapus folder beserta isinya


def yt_downloader(yt_url):
    delete_folder()

    try:
        yt = YouTube(yt_url)
        title = yt.title
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path=DONWLOAD_FOLDER, filename=f"{title}.mp4")

        return title
    except Exception as e:
        e


def save_uploaded_file(uploaded_file, save_dir=DONWLOAD_FOLDER):
    delete_folder()

    up_video = os.path.join(save_dir, uploaded_file.name)

    with open(up_video, "wb") as f:
        f.write(uploaded_file.getbuffer())

    vid_name = os.path.basename(uploaded_file.name)
    return up_video, vid_name
