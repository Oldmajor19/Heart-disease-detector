import numpy as np
import pickle
from flask import Flask, request, render_template

# Load model
model = pickle.load(open('finalized_model.sav', 'rb'))

# Create application
app = Flask(__name__)


# Bind home function to URL
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods =['POST'])
def predict():
    features = [float(i) for i in request.form.values()]
    features = np.array(features)
    features = features.reshape(1,-1)
    result = model.predict(features)

    prediction = result
    print(result)
    print(features)

    # Check the prediction values and retrive the result with html tag based on the value
    if prediction == 1:
        return render_template('index.html', 
                               result = 'The patient is not likely to have heart disease!')
    else:
        return render_template('index.html', 
                               result = 'The patient is likely to have heart disease!')
    return render_template('index.html')


if __name__ == '__main__':
#Run the application
    app.run()
