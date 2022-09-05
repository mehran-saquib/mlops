
from fastapi import FastAPI
import numpy as np
import pandas as pd
from variables import columns
import predictor
import math
import uvicorn


app=FastAPI()

@app.get('/')
def index():
    return 'Welcome to Airbnb price prediction'

@app.get('/predict')
def prediction(data:columns):
    data=data.dict()
    property_type=data['property_type']
    room_type=data['room_type']
    accommodates=data['accommodates']
    bathrooms=data['bathrooms']
    bed_type=data['bed_type']
    cancellation_policy=data['cancellation_policy']	
    cleaning_fee=data['cleaning_fee']
    city=data['city']
    instant_bookable=data['instant_bookable']
    bedrooms=data['bedrooms']
    beds=data['beds']

    prediction_value=predictor.predict(property_type,room_type,accommodates,bathrooms,bed_type,
                        cancellation_policy,cleaning_fee,city,instant_bookable,bedrooms,beds)
    # prediction_value=math.exp(prediction_value)
    return f'The log price of the airbnb property in accordance with the given attributes is {round(prediction_value,6)}'
    #return {'prediction_value':int(prediction_value)}
    # return type(property_type)

if __name__=="__main__":
    uvicorn.run("api:app",port=8000,reload=True)




