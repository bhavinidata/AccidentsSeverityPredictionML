# US Accidents severity Prediction

### Data Source: 
Kaggle. Dataset contains US traffic data from Feb 2016 to March 2019.

### Description: 
This project is used to predict US traffic accidents severity based on weather conditions like visibility, temperature, and weather categories as well as based on US location and the day of the week. This project can be used for numerous applications such as real-time accident severity prediction based on environment factors. Studying accident hotspot locations and their severity.

* Rich data with almost 2 million rows
* Needed pre-processing (Spark) 
* Severity contained in data is prone to errors 
* Weather condition categorization may not be accurate 
* Data is imbalanced 


### Data Cleaning: 
* Select important features and remove unnecessary columns.
* Remove the rows with null values.
* Do data profiling to validate correctness of data.

### Data Preprocessing: 
* Convert columns with text field to numerical data.
* Categorized weather conditions 
* Eliminated rows that greatly contributed to the imbalance of the data and were not significant in volume
* Replaced null values with fillers 

### Features:
Latitude, Longitude, Temperature(F), Visibility(mi), Weather_Category(Rain, Cloudy, slippery etc..), Weekday

### Machine Learning Models:
* Logistic Regression
* Random Forest
* SVM

### Attempts to achieve good accuracy
* Did Hyper Parameter Tuning using Grid Search  
* Trained the model with 75% of data 
* Tested Accuracy for all models using test data 
* Generated classification reports 
* Generated feature importance 
* Random Under Sampler to balance data (imb learn)

### Result from every Model:
* Logistic Regression
    * Training Accuracy: 35%
    * Testing Accuracy: 35%
    
* Support Vector Classifier
    * Training Accuracy: 36.7%
    * Testing Accuracy: 35.4%

* Model-3 Random Forest with grid search (n_estimator: 10,  max_depth: 75) and over sampling -SMOTE
    * Training Accuracy: 93%
    * Testing Accuracy: 73%
    Due to overtraining the model, it has not been used even though it gives high accuracy.

* Model-4 Random Forest with grid search (n_estimator:10, max_depth: 20) and over sampling -SMOTE
    * Training Accuracy: 77.7%
    * Testing Accuracy: 69.9%

                  pre       rec        f1       


          2       0.85      0.71       0.77      
          3       0.58      0.69       0.63      
          4       0.21      0.52       0.30     

    avg / total   0.74             0.70            0.71 


* Model-5 Random Forest with grid search (n_estimator: 10, max_depth: 75) and under sampling-  RandomUnderSampler
    * Training Accuracy: 65%
    * Testing Accuracy: 61.91%


                  pre       rec          f1       


          2       0.83      0.63        0.72      
          3       0.54      0.58        0.56      
          4       0.14      0.71        0.23     

avg / total         0.72           0.62             0.65 


###### Finally Model-4 Random Forest with grid search (n_estimator:10, max_depth: 20) and over sampling -SMOTE has been used to predict the accident severity.


### Tools and Technology:
* Jupyter notebook, AWS-Postgres, Databricks, PySpark, Pandas, Scikit-learn, FLASK, Tableau

### Team Members:
* Ahmar Jamal
* Bhavini Vyas
* Rutabah Khan

