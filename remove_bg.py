import streamlit as st
from rembg import remove 
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout = "wide", page_title = "Remove BG")

st.write("## 🎗️ Remove Background from your Image 🎗️")
st.write("Try uploading an image and watch the background removed magically with ease✨")
st.sidebar.write("## REMOVE BG 🍒")

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("ORIGINAL IMAGE :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("REMOVED BG IMAGE 🪄")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download image", convert_image(fixed), "remove_bg.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("./shiba_inu.jpg")