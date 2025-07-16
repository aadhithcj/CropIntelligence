from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the trained model, scaler, and label encoder
try:
    with open(r"D:\ICT Project\kerala-crop-oracle\kerala-crop-oracle\flask_backend\best_model.pkl", "rb") as f:
        model = pickle.load(f)
    
    with open(r"D:\ICT Project\kerala-crop-oracle\kerala-crop-oracle\flask_backend\scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    with open(r"D:\ICT Project\kerala-crop-oracle\kerala-crop-oracle\flask_backend\label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)
    
    print("Models loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")
    model = None
    scaler = None
    label_encoder = None

# District mapping for Kerala
DISTRICT_MAPPING = {
    'Thiruvananthapuram': 'district_thiruvananthapuram',
    'Kollam': 'district_kollam', 
    'Pathanamthitta': 'district_pathanamthitta',
    'Idukki': 'district_idukki',
    'Kottayam': 'district_kottayam',
    'Ernakulam': 'district_ernakulam',
    'Thrissur': 'district_thrissur',
    'Palakkad': 'district_palakkad',
    'Malappuram': 'district_malappuram',
    'Kozhikode': 'district_kozhikode',
    'Wayanad': 'district_wayanad',
    'Kannur': 'district_kannur'
}

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'models_loaded': model is not None and scaler is not None and label_encoder is not None
    })

@app.route('/api/predict', methods=['POST'])
def predict_crop():
    try:
        if not all([model, scaler, label_encoder]):
            return jsonify({'error': 'Models not loaded properly'}), 500
        
        data = request.json
        
        # Extract input parameters
        year = data.get('year', 2024)
        rainfall = data.get('rainfall', 2500)
        monsoon = data.get('monsoon', rainfall * 0.6)  # Estimate monsoon as 60% of total rainfall
        score = data.get('score', 0.75)  # Default agricultural score
        district = data.get('district', 'Ernakulam')
        
        # Create input dataframe
        input_data = pd.DataFrame([{
            "year": year,
            "rainfall": rainfall,
            "monsoon": monsoon,
            "score": score,
            'district_ernakulam': 0,
            'district_idukki': 0,
            'district_kannur': 0,
            'district_kollam': 0,
            'district_kottayam': 0,
            'district_kozhikode': 0,
            'district_malappuram': 0,
            'district_palakkad': 0,
            'district_pathanamthitta': 0,
            'district_thiruvananthapuram': 0,
            'district_thrissur': 0,
            'district_wayanad': 0,
        }])
        
        # Set the appropriate district to 1
        district_col = DISTRICT_MAPPING.get(district)
        if district_col and district_col in input_data.columns:
            input_data[district_col] = 1
        
        # Ensure all expected columns are present
        expected_columns = scaler.feature_names_in_
        for col in expected_columns:
            if col not in input_data.columns:
                input_data[col] = 0
        
        # Reorder columns to match training data
        input_data = input_data[expected_columns]
        
        # Scale the input data
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction_encoded = model.predict(input_scaled)
        prediction_proba = model.predict_proba(input_scaled)
        
        # Decode the prediction
        prediction_label = label_encoder.inverse_transform(prediction_encoded)
        confidence = float(np.max(prediction_proba) * 100)
        
        return jsonify({
            'predicted_crop': prediction_label[0],
            'confidence': round(confidence, 2),
            'input_params': {
                'year': year,
                'rainfall': rainfall,
                'monsoon': monsoon,
                'score': score,
                'district': district
            }
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)