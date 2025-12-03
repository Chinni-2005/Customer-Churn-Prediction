# 📊 Customer Churn Analysis & Prediction

A complete end-to-end **EDA → Model Building → Model Deployment** project using **Python, Machine Learning & Flask**.

---

## 🔥 Project Overview

This project focuses on analyzing telecom customer behavior to identify factors that lead to **customer churn**.
The workflow includes:

* ✔️ Exploratory Data Analysis (EDA)
* ✔️ ML Model Building (Random Forest Classifier)
* ✔️ Flask-based deployment for real-time prediction
* ✔️ Simple front-end UI for user input

---

## 📌 Understanding Customer Churn

Customer Churn refers to the percentage of subscribers who discontinue using a service during a specific period.
This project visualizes:

* Churn scenarios
* Decision cycles
* Churn segments
* Customer behavior insights



## 📁 Repository Structure

| File                                      | Description                                   |
| ----------------------------------------- | --------------------------------------------- |
| **Churn Analysis - EDA.ipynb**            | Exploratory Data Analysis & insights          |
| **Churn Analysis - Model Building.ipynb** | Preprocessing, ML model training & evaluation |
| **app.py**                                | Flask backend for model deployment            |
| **home.html**                             | Frontend UI for prediction                    |
| **model.pkl**                             | Trained ML model                              |
| **model_columns.pkl**                     | Training feature columns                      |

---

## 🧠 Solution Architecture
![Solution](https://github.com/Chinni-2005/Customer-Churn-Prediction/blob/589060a1f0d4fce0afeee15490c830d3ece10c31/images/Telco5.JPG)

---

# 🚀 Flask Deployment Instructions

### 1️⃣ Create the Flask App

```python
app = Flask("__name__")
```

### 2️⃣ Load the Home Page

```python
@app.route("/")
def loadPage():
    return render_template('home.html', query="")
```

### 3️⃣ Handle Prediction (POST Request)

```python
@app.route("/", methods=['POST'])
def predict():
```

### 4️⃣ Run the Application

```python
app.run()
```

Open terminal / Anaconda Prompt and run:

```bash
python app.py
```

You will see:

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Open the link in your browser to test the app.

---

## 🖼️ Frontend Preview

![Frontend](https://github.com/Chinni-2005/Customer-Churn-Prediction/blob/589060a1f0d4fce0afeee15490c830d3ece10c31/images/Project%20Interface.png)
---

## 🏁 Final Notes

This project gives a complete cycle from **data understanding → prediction → deployment**.
You can extend the model by:

* Adding hyperparameter tuning
* Using XGBoost / LightGBM
* Deploying on AWS / Render / Railway

---
