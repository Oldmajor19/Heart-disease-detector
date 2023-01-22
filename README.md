# Heart Disease Prediction
### This project aims to predict the presence of heart disease in a patient using machine learning. The dataset used for this project is the UCI Heart Disease dataset available on Kaggle. The dataset contains various medical attributes of patients and a label indicating whether or not they have heart disease.

### Project Overview
The project is implemented in Python and uses various libraries such as pandas, numpy, matplotlib, seaborn, and sklearn. The data has been preprocessed, and different models were trained and evaluated. The best performing model was then deployed as a web app using Streamlit.

### Data Overview
The data contains 303 observations, 14 attributes, and 1 target variable. The attributes are:

* age
* sex
* chest pain type (4 values)
* resting blood pressure
* serum cholestoral in mg/dl
* fasting blood sugar > 120 mg/dl
* resting electrocardiographic results (values 0,1,2)
* maximum heart rate achieved
* exercise induced angina
* oldpeak = ST depression induced by exercise relative to rest
* the slope of the peak exercise ST segment
* number of major vessels (0-3) colored by flourosopy
* thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
* The target variable is binary, and indicates whether or not the patient has heart disease (1 = Yes, 0 = No).

### Deployment
This project uses Flask API to deploy the model and build the web application.

### Requirements
* pandas
* numpy
* matplotlib
* seaborn
* sklearn
* check requirements.txt


### File Descriptions
* heart.csv is the dataset file
* heart_disease.ipynb: contains the code of data exploration, preparation and modeling.
* finalized_model.sav: Is the best performing classisfication model
* index.py: Flask API that bind between the classification model and the web page.
### Conclusion
This project demonstrates how machine learning can be used to predict the presence of heart disease in a patient. The deployed model can be used as a tool to assist doctors in the diagnosis of heart disease.
