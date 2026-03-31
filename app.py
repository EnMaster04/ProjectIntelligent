import streamlit as st

# ตั้งค่า page
st.set_page_config(
    page_title="AI Project",
    page_icon="🤖",
    layout="centered"
)

# Header
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>
        🤖 Intelligent System Project
    </h1>
    """,
    unsafe_allow_html=True
)

# ข้อมูลผู้จัดทำ
st.markdown("---")
st.markdown("### 👨‍🎓 ข้อมูลผู้จัดทำ")
st.write("**รหัสนักศึกษา:** 6704062612316")
st.write("**ชื่อ:** กฤษณพงศ์ แก้วฝั้น")
st.write("**มหาวิทยาลัย:** มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ")
st.write("**รายวิชา:** Intelligent System")

# แหล่งที่มา Dataset
st.markdown("---")
st.markdown("###  แหล่งที่มา Dataset")
st.write("**kaggle:** Dog vs Cat")
st.write("**kaggle:** Credit Card Fraud Detection")
st.write("**readme:** ลิงค์Google Driveใน README เนื่องจากไฟล์Dataset มีขนาดใหญ่เกินไปสำหรับการอัปโหลดโดยตรงในGithub")

# Section 1: Fraud Detection
st.markdown("---")
st.markdown("### 💳 ระบบตรวจจับธุรกรรมโกง (Fraud Detection)")
st.info("ใช้ Machine Learning วิเคราะห์ธุรกรรมว่าเป็น Fraud หรือ Normal")
st.markdown("""
- วิเคราะห์ข้อมูลธุรกรรมจากไฟล์ `creditcard.csv`
- ใช้โมเดลเช่น Random Forest / SMOTE
- แสดงผลว่าเป็น **Fraud** หรือ **Normal**
""")

# Section 2: Image Classification
st.markdown("---")
st.markdown("### 🐶🐱 ระบบแยกภาพหมาแมว (Dog vs Cat)")
st.success("ใช้ Neural Network (CNN) ในการจำแนกรูปภาพ")
st.markdown("""
- รับภาพจากผู้ใช้
- ใช้โมเดล CNN วิเคราะห์
- แสดงผลว่าเป็น **Dog 🐶** หรือ **Cat 🐱**
""")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)