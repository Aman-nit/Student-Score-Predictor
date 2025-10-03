from flask import Flask,request, render_template
import numpy as np
import pandas as pd
import sys

from sklearn.preprocessing import StandardScaler
from src.pipeline.predit_pipeline import PredictPipeline, CustomData

application= Flask(__name__)

app = application

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST','GET'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        print("Inside /predict route")

        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        pred_df = data.get_as_dataFrame()
        print("Prediction DataFrame:\n", pred_df)

        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(features=pred_df)

        return render_template('home.html', result=result[0])

    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)