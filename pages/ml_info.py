import streamlit as st

st.set_page_config(page_title="Fraud Detection", page_icon="💳", layout="centered")

# Header
st.markdown("""
<h1 style='text-align: center; color: #1E88E5;'>
💳 Machine Learning Model (Fraud Detection)
</h1>
""", unsafe_allow_html=True)

# Dataset
st.markdown("---")
st.markdown("### 📂 Dataset")
st.info("Credit Card Fraud Detection จาก Kaggle")

st.write("""
🔗 https://www.kaggle.com/datasets/kornilovag94/payment-systems-transactions-synthetic-dataset  

ใช้ข้อมูลธุรกรรมเพื่อตรวจสอบว่าเป็น Fraud หรือ Normal
""")

# Features
st.markdown("---")
st.markdown("### 📊 Feature Dataset")

st.write("""
1. step → จำนวนครั้งของธุรกรรม  
   - min: 1 | max: 743 | mean: 243  

2. type → ประเภทธุรกรรม  
   - cash_out (35%)  
   - payment (34%)  
   - other (31%)  

3. amount → จำนวนเงิน  
   - min: 0 | max: 92.4M | mean: 180K  

4. nameOrig → บัญชีต้นทาง  
5. oldbalanceOrg → เงินก่อนทำรายการ (ต้นทาง)  
6. newbalanceOrg → เงินหลังทำรายการ (ต้นทาง)  
7. nameDest → บัญชีปลายทาง  
8. oldbalanceDest → เงินก่อนทำรายการ (ปลายทาง)  
9. newbalanceDest → เงินหลังทำรายการ (ปลายทาง)  
10. isFraud → ผลลัพธ์ (โกง / ไม่โกง)
""")

# Preprocessing
st.markdown("---")
st.markdown("### ⚙️ การเตรียมข้อมูล")

st.success("""
1. เลือก Feature สำคัญ เช่น Amount, V14, V12, V10  
2. แก้ปัญหา Class Imbalance ด้วย SMOTE  
3. แบ่งข้อมูลด้วย train_test_split()
""")

st.code("""
features = ["Amount", "V14", "V12", "V10"]
X = df[features]
y = df["Class"]
""", language="python")

# Algorithm
st.markdown("---")
st.markdown("### 🧠 อัลกอริทึมที่ใช้")

st.warning("""
ใช้หลายโมเดลร่วมกัน (Ensemble)

- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Random Forest  

ใช้ Voting Classifier ในการตัดสินผล
""")

# Steps
st.markdown("---")
st.markdown("### 🔄 ขั้นตอนการพัฒนาโมเดล")

st.write("""
1. โหลดข้อมูล → pd.read_csv()  
2. เลือก Feature  
3. แก้ Imbalance → SMOTE  
4. แบ่ง Train/Test  
5. Train → model.fit()  
6. Evaluate → classification_report()  
7. Save Model → pickle.dump()  
8. Deploy → ใช้ใน Web App  
""")

# Usage
st.markdown("---")
st.markdown("### 🚀 วิธีการใช้งาน")
st.info("กรอกจำนวนเงิน เพื่อวิเคราะห์ว่าเป็น Fraud หรือ Normal")

# Reference
st.markdown("---")
st.markdown("### 📚 แหล่งอ้างอิง")

st.write("""
1. ChatGPT  
2. เอกสารการสอนของ Dr. Nattagit Jiteurtragool (NJR)  
""")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)