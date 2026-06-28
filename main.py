import uvicorn
from fastapi import FastAPI,Request ##ASGI
import joblib
import pandas as pd
from pydantic import BaseModel,Field
from typing import Literal
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import numpy as np

#importing the ml model
model = joblib.load('battery_rul_champion_rf.pkl')

app = FastAPI(
    title="Battery Remaining Useful Life (RUL) Predictor",
    description="API to predict battery cycle degradation using optimized Random Forest regression."
)

templates = Jinja2Templates(directory="templates")

#building pydantic model
class BatteryFeatures(BaseModel):
    discharge_time: float = Field(
        description="Total battery discharge duration in seconds. Expects values from a typical cycle.",
        gt=0,
        json_schema_extra={"examples": [2150.0]}
    )
    decrement_range: float = Field(
        description="Time taken (in seconds) for the battery voltage to drop specifically from 3.6V down to 3.4V.",
        ge=0,
        json_schema_extra={"examples": [1150.0]}
    )
    max_voltage_discharge: float = Field(
        description="The peak voltage measured during the discharge phase. Must be between 2.0V and 5.0V.",
        gt=2.0, 
        lt=5.0,
        json_schema_extra={"examples": [4.02]}
    )
    min_voltage_charge: float = Field(
        description="The lowest voltage measured when the charging phase initiated. Must be between 1.0V and 5.0V.",
        gt=1.0, 
        lt=5.0,
        json_schema_extra={"examples": [3.36]}
    )
    time_at_voltage_threshold: float = Field(
        description="Time spent at or above the high voltage threshold of 4.15V in seconds.",
        ge=0,
        json_schema_extra={"examples": [20.0]}
    )
    time_constant_current: float = Field(
        description="Duration in seconds of the Constant Current (CC) charging mode before switching to Constant Voltage.",
        ge=0,
        json_schema_extra={"examples": [620.0]}
    )
    charging_time: float = Field(
        description="Total overall battery charging duration in seconds.",
        gt=0,
        json_schema_extra={"examples": [5100.0]}
    )

    model_config = {
        "populate_by_name": True
    }
    
@app.get('/', response_class=HTMLResponse)
def serve_website(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/health', tags=["System Monitoring"])
def health_check():
    return JSONResponse(
        status_code=200,
        content={
            "status": "OK",
            "model_loaded": model is not None,
            "version": "1.0.0"
        }
    )

@app.post('/predict')
def predict_rul(data: BatteryFeatures):

    input_df = pd.DataFrame([{
        'Discharge Time (s)':data.discharge_time,
        'Decrement 3.6-3.4V (s)':data.decrement_range,
        'Max. Voltage Dischar. (V)':data.max_voltage_discharge,
        'Min. Voltage Charg. (V)':data.min_voltage_charge,
        'Time at 4.15V (s)':data.time_at_voltage_threshold,
        'Time constant current (s)':data.time_constant_current,
        'Charging time (s)':data.charging_time
    }])

    main_prediction = model.predict(input_df)[0]
    # model.estimators_ contains all the individual decision trees
    tree_predictions = [estimator.predict(input_df.values)[0] for estimator in model.estimators_]
    # This represents the disagreement/uncertainty of the forest[std]
    prediction_std = np.std(tree_predictions)
    
    #Calculating a 95% Confidence Interval margin (approx. 1.96 * standard deviation)
    margin_of_error = 1.96 * prediction_std

    # Defining lower and upper confidence limits
    lower_bound = max(0, main_prediction - margin_of_error)
    upper_bound = main_prediction + margin_of_error

    return JSONResponse(
        status_code=200, 
        content={
            'Predicted RUL': round(float(main_prediction), 2),
            'Confidence Analytics': {
                'Margin of Error (cycles)': round(float(margin_of_error), 2),
                '95% Confidence Interval': [round(float(lower_bound), 2), round(float(upper_bound), 2)],
                'Model Disagreement Standard Deviation': round(float(prediction_std), 2)
            }
        }
    )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)




