import pickle
import pandas as pd
import numpy as np
import config 
import sklearn
import warnings
import json
warnings.filterwarnings('ignore')

class Insurance():
    def __init__(self,age, gender, bmi, children, smoker, region):
        self.age = age
        self.gender = gender
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = "region_" + region

    def load_saved_data(self):    
        with open(r"lin_reg.pkl","rb") as f:
            self.model = pickle.load(f)   

        with open(r"predict_data.json",'r') as r:
            self.project_data = json.load(r)   

    def get_pred_value(self):   
        self.load_saved_data()

        # gender = self.project_data['gender'][self.gender]
        # smoker = self.project_data['smoker'][self.smoker]#region = "region_"+ region
        region_index = self.project_data['column'].index(self.region)
        # print('region_index :',region_index)
       
        col_count = len(self.project_data['column'])
        array = np.zeros(col_count)

        array[0] = self.age
        array[1] = self.project_data['gender'][self.gender]
        array[2] = self.bmi
        array[3] = self.children
        array[4] = self.project_data['smoker'][self.smoker]
        array[region_index] = 1 
        print(array)
        predicted_value = np.around(self.model.predict([array])[0],2)
        print("The Insurance Amount Is:",np.around(np.exp(predicted_value),2))
            
        return predicted_value

if __name__ == '__main__':
    obj = Insurance()
    obj        
       