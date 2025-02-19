import joblib
import numpy as np
import pandas as pd
from pathlib import Path 


class PredictionPipeline:
    def __init__(self, model_path: str):
        self.model=joblib.load(Path("D:\\Udemy\\ML_Bootcamp\\18_End_to_End_DataScience_Project\\datascienceproject\\artifacts\\model_trainer\\model.joblib"))
        
    def predict(self,data):
        prediction= self.model.predict(data)
        
        
        return prediction