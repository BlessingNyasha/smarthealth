import pickle
import numpy as np
import pandas as pd
from joblib import dump, load

save_path = "saved_model/"


model_name = "model"
model2_name = "model2"

model = load(str(model_name + ".joblib"))
model2 = load(str(model2_name + ".joblib"))

def predictly(inputs):

    


    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(inputs)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
        resultly = 'You do not have a Heart Disease'
        return resultly
    else:
        resultly = 'Your results shows signs of a has Heart Disease.  Get to a doctor for further analysis'
        return resultly
    
def prediction(inputs):

    


    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(inputs)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model2.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 1):
        resultl = 'Your lungs are in the normal capacity of your age '
        return resultl
    else:
        resultl = 'Get your Lungs checked for Obstruction-Obstructive diseases: such as asthma and COPD result in obstructed airways. This creates airway resistance to expiratory flow, so the patient struggles to get air out quickly and has a decreased FEV1. A smaller FEV1 also results in a smaller FEV1/FVC ratio.  or Restrictive lung conditions-Restrictive diseases such as pulmonary fibrosis/interstitial lung disease, obesity, neuromuscular and chest/spine deformitiesrestrict lung expansion, reducing the amount of air the lungs can hold (the vital capacity). This means the patient has a lower FVC. As there is decreased compliance and elasticity, it is also harder for the lungs to force air out quickly, resulting in a decreased FEV1. As both the FEV1 and the FVC have decreased, the FEV1/FVC ratio remains near normal.'
        return resultl