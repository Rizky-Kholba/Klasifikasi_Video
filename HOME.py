import streamlit as st
from PIL import Image
import base64

# Pengaturan Halaman
st.set_page_config(
    page_title="Klasifikasi Topik Video",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="expanded",
)


# Fungsi untuk Mengubah Gambar menjadi Base64
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Mengatur Gambar Logo
image_path = "logo.png"
image_base64 = get_image_base64(image_path)
logo_html = f"""
<div style='text-align: center;'>
    <img src='data:image/png;base64,{image_base64}' width='300' alt='Klasifikasi Topik Video'>
</div>
"""

# Judul Halaman
st.title("🎥 Klasifikasi Topik Video")

# Deskripsi Singkat
st.write(
    """
Selamat datang di aplikasi Klasifikasi Topik Video! Aplikasi ini dirancang untuk membantu Anda mengklasifikasikan 
video ke dalam berbagai topik menggunakan teknologi machine learning. Dengan mengunggah video, Anda dapat 
mengetahui topik apa yang terkait dengan video tersebut.
"""
)

# Menampilkan Gambar atau Logo di Tengah
st.markdown(logo_html, unsafe_allow_html=True)

# Fitur Aplikasi
st.header("Fitur Aplikasi")
st.write(
    """
- **Klasifikasi Otomatis**: Aplikasi ini menggunakan algoritma Suppoer Vector Machine (SVM) untuk mengklasifikasikan video anda secara otomatis.
- **Kategori Topik**: Kategori yang digunakan News yaitu “olahraga”, “hiburan”, “bisnis:”, “dunia”, “nasional” dan “kesehatan”.  
"""
)

# Panduan Penggunaan
st.header("Panduan Penggunaan")
st.write(
    """
1. **Pilih Sumber Video**: Pilih sumber video yang ingin diklasifikasi pada menu "Sumber Video".
2. **Unggah Video**: Unggah video sesuai dengan sumber yang diinginkan.
3. **Proses Klasifikasi**: Klik tomboh "Mulai Proses" lalu tunggu beberapa saat hingga proses klasifikasi selesai.
4. **Lihat Hasil**: Hasil klasifikasi akan ditampilkan secara otomatis.
"""
)


# Catatan Hak Cipta
st.write("---")
st.write("© 2024 -MR.K, STT WASTUKANCANA.")
