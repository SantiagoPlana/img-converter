import streamlit as st
from PIL import Image
from io import BytesIO

def to_bytes(image, format):
    buf = BytesIO()
    image.save(buf, format=format)
    byte_im = buf.getvalue()
    return byte_im


st.subheader('Conversor de imagen a escala de grises')
upload = st.file_uploader('Subir imagen')
radio_1 = st.radio('Tipo de conversión', options=['L', '1', 'RGB', 'CMYK'], key='radio_descarga')
radio_2 = st.radio('Extensión del archivo', options=['JPEG', 'PNG'], key='radio_ext')
if upload:
    img = Image.open(upload)
    gray_img = img.convert(radio_1)
    download_img = to_bytes(gray_img, radio_2)
    st.image(gray_img)
    st.download_button('Descargar imagen convertida', key='descargar_1',
                       data=download_img, file_name=f'nueva_imagen.{radio_2}')


with st.expander('Iniciar cámara'):
    imagen = st.camera_input('Camera')

if imagen:
    radio = st.radio('Tipo de conversión',
                     options=['L', '1', 'RGB', 'CMYK'], key='radio_captura')

    img = Image.open(imagen)
    gray_img = img.convert(radio)

    st.image(gray_img)

    download_img = to_bytes(gray_img)

    st.download_button('Descargar imagen', key='descargar',
                       data=download_img, file_name='nueva_imagen.jpeg')