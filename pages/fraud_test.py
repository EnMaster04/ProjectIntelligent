import streamlit as st
import numpy as np
import random
import joblib
import os

# โหลด model
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, "..", "fraud_model.pkl")

model = joblib.load(model_path)

st.set_page_config(page_title="Fraud Detection AI", layout="centered")

st.title("💳 AI Fraud Detection System")
st.write("กรอกจำนวนเงิน ระบบจะประเมินความเสี่ยงอัตโนมัติ")

# input
amount = st.number_input(
    "💰 Amount",
    min_value=0.0,
    max_value=92_000_000.0,   # 10 ล้าน
    value=100.0,
    step=10.0
)

if st.button("🔍 Analyze Transaction"):

    if amount > 92_000_000:
        st.warning("⚠️ Amount ต้องไม่เกิน 92,000,000")
    else:
        # สร้าง feature 
        if amount > 100000:
            v14 = random.uniform(-6,-3)
            v12 = random.uniform(-5,-2)
            v10 = random.uniform(-6, -3)
        elif amount > 10000:
            v14 = random.uniform(-4,-1)
            v12 = random.uniform(-3,0)
            v10 = random.uniform(-4,-1)
        else:
            v14 = random.uniform(-1,3)
            v12 = random.uniform(-1,3)
            v10 = random.uniform(-1,3)

        input_data = np.array([[amount, v14, v12, v10]])

        # predict
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_data)[0][1]
        else:
            pred = model.predict(input_data)[0]
            proba = float(pred)

        fraud_percent = proba * 100
        normal_percent = (1 - proba) * 100

        # threshold
        if proba > 0.45:
            st.error(f"🚨 Fraud Detected ({fraud_percent:.2f}%)")
        else:
            st.success(f"✅ Normal Transaction ({normal_percent:.2f}%)")

        st.write("### Risk Level")
        st.progress(int(fraud_percent))