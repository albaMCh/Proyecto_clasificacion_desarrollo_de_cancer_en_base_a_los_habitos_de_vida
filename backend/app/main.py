# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model
import sys
from pathlib import Path

# Create the app
app = FastAPI()

#dir = path.Path(__file__).abspath()
#sys.path.append(dir.parent.parent)

# Load trained Pipeline

path = Path(__file__).parent / 'knn'
print('==================================')
print(path)
model = load_model(path)

# Create input/output pydantic models
input_model = create_model("knn_input", **{'Patient Id': 'P789', 'Age': 39, 'Gender': 2, 'Air Pollution': 6, 'Alcohol use': 8, 'Dust Allergy': 7, 'OccuPational Hazards': 7, 'Genetic Risk': 7, 'chronic Lung Disease': 6, 'Balanced Diet': 7, 'Obesity': 7, 'Smoking': 8, 'Passive Smoker': 7, 'Chest Pain': 7, 'Coughing of Blood': 9, 'Fatigue': 3, 'Weight Loss': 2, 'Shortness of Breath': 4, 'Wheezing': 1, 'Swallowing Difficulty': 4, 'Clubbing of Finger Nails': 2, 'Frequent Cold': 4, 'Dry Cough': 2, 'Snoring': 3})
output_model = create_model("knn_output", prediction='Low')


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


#if __name__ == "__main__":
#   uvicorn.run(app, host="127.0.0.1", port=8000)
