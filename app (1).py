# coding: utf-8

import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# ✅ Load model and training columns once at startup
model = pickle.load(open("model.sav", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

# ✅ GET route – show homepage
@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")


# ✅ POST route – handle prediction form
@app.route("/", methods=['POST'])
def predict():
    try:
        # Collect all 19 input values from form
        input_values = [request.form.get(f'query{i}') for i in range(1, 20)]

        # Create DataFrame with correct column names
        new_df = pd.DataFrame([input_values], columns=[
            'SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender', 
            'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService',
            'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
            'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
            'PaymentMethod', 'tenure'
        ])

        # ✅ Convert numeric columns
        numeric_cols = ['SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'tenure']
        for col in numeric_cols:
            new_df[col] = pd.to_numeric(new_df[col], errors='coerce').fillna(0)

        # ✅ Create tenure group
        labels = [f"{i} - {i + 11}" for i in range(1, 72, 12)]
        new_df['tenure_group'] = pd.cut(new_df.tenure.astype(int), range(1, 80, 12),
                                        right=False, labels=labels)
        new_df.drop(columns=['tenure'], axis=1, inplace=True)

        # ✅ Get dummies for the new input only
        new_df_dummies = pd.get_dummies(new_df)

        # ✅ Align with model columns (fill missing with 0)
        new_df_dummies = new_df_dummies.reindex(columns=model_columns, fill_value=0)

        # ✅ Make prediction
        prediction = model.predict(new_df_dummies)[0]
        probability = model.predict_proba(new_df_dummies)[0][1]

        if prediction == 1:
            o1 = "This customer is likely to be churned!!"
        else:
            o1 = "This customer is likely to continue!!"

        o2 = f"Confidence: {probability * 100:.2f}%"

        # ✅ Render result on the page
        return render_template(
            'home.html',
            output1=o1,
            output2=o2,
            **{f"query{i}": request.form.get(f"query{i}", "") for i in range(1, 20)}
        )

    except Exception as e:
        return render_template("home.html", output1="Error occurred", output2=str(e))


if __name__ == "__main__":
    app.run(debug=True)
