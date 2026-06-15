from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    pregnancies = float(request.form["Pregnancies"])
    glucose = float(request.form["Glucose"])
    blood_pressure = float(request.form["BloodPressure"])
    skin_thickness = float(request.form["SkinThickness"])
    insulin = float(request.form["Insulin"])
    bmi = float(request.form["BMI"])
    dpf = float(request.form["DiabetesPedigreeFunction"])
    age = float(request.form["Age"])

    # Feature Engineering
    bmi_age = bmi * age
    glucose_bmi = glucose * bmi

    health_index = (
        0.4 * glucose +
        0.3 * bmi +
        0.3 * age
    )

    features = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        dpf,
        age,
        bmi_age,
        glucose_bmi,
        health_index
    ]])

    prediction = model.predict(features)[0]

    probability = round(
        model.predict_proba(features)[0][1] * 100,
        2
    )

    if prediction == 1:
        result = "⚠️ High Diabetes Risk"
    else:
        result = "✅ Low Diabetes Risk"

    return render_template(
        "index.html",
        prediction=result,
        probability=probability
    )


if __name__ == "__main__":
    app.run(debug=True)
