from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('sales_prediction_model.pkl')

# Define the feature names as per your trained model
FEATURES = ['Paid_Views', 'Organic_Views', 'Google_Impressions', 'Email_Impressions', 
            'Facebook_Impressions', 'Affiliate_Impressions', 'Overall_Views', 
            'Month', 'Week', 'Day', 'Google_Impression_Ratio', 
            'Facebook_Impression_Ratio', 'Email_Impression_Ratio']

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON request data
        data = request.json
        
        # Ensure the input data has all required features
        input_data = pd.DataFrame([data], columns=FEATURES)
        
        # Make predictions
        prediction = model.predict(input_data)
        
        # Return the prediction as JSON
        return jsonify({'prediction': prediction[0]})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
