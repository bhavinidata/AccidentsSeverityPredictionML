from flask import Flask, render_template, request, url_for
import requests
# from treat_data import treat_input
import json
from sklearn.externals import joblib
import numpy as np

application = Flask(__name__)

@application.route('/')
@application.route('/index')
def home():
    return render_template('index.html')

#  prediction function 
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 6) 
    loaded_model = joblib.load(open("model/final_acc_sev_pred_grid.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result[0] 
  
@application.route('/result', methods = ['POST']) 
def result(): 
    print("In RESULTS:")
    if request.method == 'POST': 
        to_predict_list = request.form.to_dict() 
        print(to_predict_list)
        to_predict_list = list(to_predict_list.values()) 
        # to_predict_list = list(map(int, to_predict_list)) 
        result = ValuePredictor(to_predict_list)         
        if int(result)== 2: 
            prediction ='Less Severe'
        elif int(result)== 3: 
            prediction ='Moderate'
        elif int(result)== 4: 
            prediction ='Severe'            
        return render_template("result.html", prediction = prediction) 


if __name__ == '__main__':
    application.run(debug=True)