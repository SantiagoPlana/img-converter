import streamlit as st
from PIL import Image
from io import BytesIO

def to_bytes(image):
    buf = BytesIO()
    image.save(buf, format='JPEG')
    byte_im = buf.getvalue()
    return byte_im


st.subheader('Conversor de imagen a escala de grises')
upload = st.file_uploader('Subir imagen')
if upload:
    img = Image.open(upload)
    gray_img = img.convert('L')
    download_img = to_bytes(gray_img)
    st.image(gray_img)
    st.download_button('Descargar imagen convertida', key='descargar_1',
                       data=download_img, file_name='grayscale.jpeg')


with st.expander('Iniciar cámara'):
    imagen = st.camera_input('Camera')

if imagen:
    radio = st.radio('Tipo de conversión',
                     options=['L', '1'])

    img = Image.open(imagen)
    gray_img = img.convert(radio)

    st.image(gray_img)

    download_img = to_bytes(gray_img)

    st.download_button('Descargar imagen', key='descargar',
                       data=download_img, file_name='grayscale.jpeg')