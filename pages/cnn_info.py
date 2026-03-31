import streamlit as st

st.set_page_config(page_title="CNN Dog vs Cat", page_icon="🐶", layout="centered")

# Header
st.markdown("""
<h1 style='text-align: center; color: #FF6F61;'>
🐶🐱 Convolutional Neural Network Model
</h1>
""", unsafe_allow_html=True)

# Dataset
st.markdown("---")
st.markdown("### 📂 Dataset")
st.info("Dog vs Cat Dataset จาก Kaggle")

st.markdown("""
🔗 https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset  

**โครงสร้างข้อมูล**
- **test/**
  - 12,500 รูป (หมา+แมวปนกัน)
  - ชื่อไฟล์: `1.jpg - 12500.jpg`
- **train/**
  - 🐱 แมว 12,500 รูป → `cat.0.jpg - cat.12499.jpg`
  - 🐶 หมา 12,500 รูป → `dog.0.jpg - dog.12499.jpg`
""")

# Preprocessing
st.markdown("---")
st.markdown("### ⚙️ การเตรียมข้อมูล (Preprocessing)")
st.success("""
1. Normalize → แปลง pixel จาก 0–255 → 0–1  
2. Resize → ปรับขนาดภาพ เช่น (150,150)  
3. Batching → แบ่งข้อมูลเป็นชุดย่อย
""")

# Algorithm
st.markdown("---")
st.markdown("### 🧠 อัลกอริทึมที่ใช้")
st.warning("""
ใช้ **CNN (Convolutional Neural Network)**

1. Convolution Layer → ดึง feature เช่น ขอบ / รูปร่าง  
2. Pooling Layer → ลดขนาดข้อมูล  
3. Fully Connected → ใช้ตัดสินผลลัพธ์  
""")

# Steps
st.markdown("---")
st.markdown("### 🔄 ขั้นตอนการพัฒนาโมเดล")
st.markdown("""
1. เตรียม Dataset (train/test)  
2. ทำ Preprocessing (resize + normalize)  
3. สร้างโมเดล CNN → `Sequential()`  
4. Train โมเดล → `model.fit()`  
5. Evaluate โมเดล  
6. Save โมเดล → `.h5`  
7. นำไปใช้ใน Web App (Predict ภาพ)  
""")

# Usage
st.markdown("---")
st.markdown("### 🚀 วิธีการใช้งาน")
st.info("อัปโหลดรูปภาพเพื่อวิเคราะห์ว่าเป็น 🐶 Dog หรือ 🐱 Cat")

# Reference
st.markdown("---")
st.markdown("### 📚 แหล่งอ้างอิง")
st.markdown("""
1. ChatGPT  
2. เอกสารการสอนของ Dr. Nattagit Jiteurtragool (NJR)  
""")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)