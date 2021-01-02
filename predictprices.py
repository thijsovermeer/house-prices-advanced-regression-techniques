from flask_restful import reqparse, Resource
import keras
import numpy as np
import json
from keras.models import load_model
from keras.wrappers.scikit_learn import KerasRegressor
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import pandas as pd

class predictprices(Resource):
    def __init__(self, model_path='API_model'):

        # setup the parser for getting house arg
        self.parser = reqparse.RequestParser()
        
        #create the key for the API call
        self.parser.add_argument('house', type=str)
        
        #loading keras model
        self.estimator = load_model(model_path)


    def get(self):
        # parse the args
        
        args = self.parser.parse_args()

        # extract the 'house' arg and pre-process 
        # to fit the shape the model expects
        house = self.__process_house(args['house'])

        # make prediction
        prediction = self.estimator.predict(house)
        
        #to convert the log output from the model to the nominal output
        prediction = np.expm1(prediction)
        # return dictionary containing the prediction
        return {'The predicted price for this house': str(prediction[0])}

    def __process_house(self, house):
        # model expects a 2d np array
        house = np.array(json.loads(house))
        house = np.array([house])
        return house
