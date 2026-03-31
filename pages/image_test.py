import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "image_model.keras")

model = tf.keras.models.load_model(model_path)

st.title("Image Classification")

file = st.file_uploader("Upload Image")

if file:
    img = Image.open(file).convert("RGB")
    img = img.resize((128,128))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)

    if pred[0][0] > 0.5:
        st.write("Dog")
    else:
        st.write("Cat")