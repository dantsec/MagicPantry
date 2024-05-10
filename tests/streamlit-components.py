import streamlit as st
# BOF >> IMAGE
import numpy as np
from PIL import Image
# EOF << IMAGE

st.title('Title')

st.header("Header")
st.subheader('Subheader')

st.divider()

st.button("Button")

st.chat_input('Chat...')

img_file_buffer = st.file_uploader('Upload a PNG image', type='png')
if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    img_array = np.array(image)
