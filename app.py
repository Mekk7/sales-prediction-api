from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('sales_prediction_model.pkl')

# Define a predict route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request in JSON format
    data = request.get_json()
    
    # Convert the JSON data into a DataFrame for the model
    input_data = pd.DataFrame([data])
    
    # Make a prediction using the loaded model
    prediction = model.predict(input_data)
    
    # Return the prediction as JSON
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
