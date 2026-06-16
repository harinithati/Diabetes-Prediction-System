# 🏥 AI Diabetes Risk Assessment Dashboard

> An AI-powered healthcare analytics dashboard that predicts diabetes risk using Machine Learning, feature engineering, and real-time risk assessment.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![XGBoost](https://img.shields.io/badge/XGBoost-ML_Model-green)
![Status](https://img.shields.io/badge/Deployment-Live-success)

---

## 🌟 Project Overview

Diabetes is one of the most prevalent chronic diseases worldwide. Early risk identification can significantly improve preventive healthcare outcomes.

This project leverages **Machine Learning and Feature Engineering** to analyze patient health indicators and estimate the probability of diabetes. The solution is deployed as an interactive web dashboard, enabling real-time predictions through a clean and intuitive interface.

---

## 🚀 Live Application

🔗 **Live Demo:**  
https://diabetes-prediction-system-0mg1.onrender.com

## 📊 Model Performance

| Metric | Value |
|----------|----------|
| Accuracy | **75.97%** |
| ROC-AUC Score | **0.829** |
| Algorithm | **XGBoost Classifier** |
| Features Used | **11** |
| Deployment | **Render Cloud Platform** |

---

## 🧠 Machine Learning Pipeline

```text
Raw Healthcare Data
          ↓
Data Cleaning
          ↓
Missing Value Treatment
          ↓
Feature Engineering
          ↓
XGBoost Training
          ↓
Model Evaluation
          ↓
Risk Prediction
          ↓
Interactive Dashboard
```

---

## 🔬 Feature Engineering

To enhance predictive performance, additional features were created:

```python
BMI_Age = BMI * Age

Glucose_BMI = Glucose * BMI

Health_Index = (
    0.4 * Glucose +
    0.3 * BMI +
    0.3 * Age
)
```

These engineered features help capture complex relationships between patient health indicators.

---

## 📁 Dataset Information

**Dataset:** Pima Indians Diabetes Dataset

### Input Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### Target Variable

```text
Outcome
```

- 0 → Non-Diabetic
- 1 → Diabetic

---

## 🎯 Key Features

✅ Real-Time Diabetes Risk Prediction

✅ Probability-Based Risk Assessment

✅ Feature Engineering Pipeline

✅ XGBoost Machine Learning Model

✅ Interactive Healthcare Dashboard

✅ Cloud Deployment using Render

✅ Responsive User Interface

---

## 🖥️ Dashboard Preview

### Main Dashboard
<img width="2780" height="1460" alt="image" src="https://github.com/user-attachments/assets/7ee65ac2-f80c-4ddc-a0f2-c6b2e0016838" />


### Prediction Example

<img width="2784" height="1462" alt="image" src="https://github.com/user-attachments/assets/17e8d8ee-9533-403c-9228-07cdf0c79669" />


## 🛠️ Technology Stack

| Category | Technologies |
|-----------|-------------|
| Programming Language | Python |
| Machine Learning | XGBoost, Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Backend | Flask |
| Frontend | HTML5, CSS3 |
| Deployment |


## 📂 Project Structure

```text
Diabetes-Prediction-System/
│
├── app.py
├── model.pkl
├── requirements.txt
├── Procfile
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/harinithati/Diabetes-Prediction-System.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd Diabetes-Prediction-System
```

### 3️⃣ Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Application

```bash
python app.py
```

### 6️⃣ Open in Browser
https://diabetes-prediction-system-0mg1.onrender.com/

## 📈 Future Enhancements

- Explainable AI using SHAP
- Risk Visualization Gauge
- PDF Health Reports
- User Authentication
- Patient History Tracking
- Database Integration
- Advanced Healthcare Analytics

---

## 💡 What Makes This Project Different?

Unlike traditional diabetes prediction projects, this solution includes:

- Feature Engineering
- Probability-Based Predictions
- Interactive Healthcare Dashboard
- Cloud Deployment
- End-to-End Machine Learning Pipeline

making it closer to a real-world healthcare analytics application.

---

## 👩‍💻 Author

**Harini Thati**

Aspiring AI & Machine Learning Engineer

Passionate about building intelligent systems that solve real-world problems through data and artificial intelligence.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
