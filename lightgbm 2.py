# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("lightgbm")

# Create input/output pydantic models
input_model = create_model("lightgbm_input", **{'Patient cId': 'P650', 'Age': 44, 'Gender': 1, 'Air Pollution': 2, 'Alcohol use': 3, 'Dust Allergy': 2, 'OccuPational Hazards': 1, 'Genetic Risk': 3, 'chronic Lung Disease': 2, 'Balanced Diet': 1, 'Obesity': 2, 'Smoking': 7, 'Passive Smoker': 6, 'Chest Pain': 2, 'Coughing of Blood': 2, 'Fatigue': 2, 'Weight Loss': 2, 'Shortness of Breath': 3, 'Wheezing': 2, 'Swallowing Difficulty': 1, 'Clubbing of Finger Nails': 2, 'Frequent Cold': 3, 'Dry Cough': 2, 'Snoring': 3})
output_model = create_model("lightgbm_output", prediction='Low')


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
