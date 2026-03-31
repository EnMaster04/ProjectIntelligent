import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier

from imblearn.over_sampling import SMOTE

# 1. โหลดข้อมูล
df = pd.read_csv("data/creditcard.csv")

# เลือก feature
features = ["Amount", "V14", "V12", "V10"]

X = df[features]
y = df["Class"]

# 2. split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. แก้ imbalance
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X_train, y_train)

# 4. สร้าง 3 โมเดล
lr = LogisticRegression(max_iter=1000, class_weight="balanced")
knn = KNeighborsClassifier(n_neighbors=5)
rf = RandomForestClassifier(
    n_estimators=120,
    class_weight="balanced",
    random_state=42
)

# 5. รวมเป็น Ensemble
model = VotingClassifier(
    estimators=[
        ('lr', lr),
        ('knn', knn),
        ('rf', rf)
    ],
    voting='soft' 
)

# 6. train
model.fit(X_res, y_res)

# 7. test
y_pred = model.predict(X_test)

print("=== Ensemble Model (LR + KNN + RF) ===")
print(classification_report(y_test, y_pred))

# 8. save
joblib.dump(model, "fraud_model.pkl")

print("Ensemble Model พร้อมใช้งาน (3 โมเดล)")