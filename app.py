from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import requests

# Initialize Flask app
app = Flask(__name__)

# Load the trained Crop Recommendation model
crop_recommendation_model_path = r'C:\Users\Gagan gowda L\Desktop\cropr\RandomForest.pkl'

try:
    with open(crop_recommendation_model_path, 'rb') as model_file:
        crop_recommendation_model = pickle.load(model_file)
    print("✅ Model loaded successfully.")
except ValueError as e:
    print("❌ Model loading failed due to version mismatch. Consider retraining the model.")
    raise e
except FileNotFoundError:
    print(f"❌ Model file not found at {crop_recommendation_model_path}. Please check the path.")
    raise FileNotFoundError(f"Model file not found at {crop_recommendation_model_path}")

# Weather API Configuration
WEATHER_API_KEY = "0dce1422df3b419bbf4110853252303"  # Your actual API key
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?"

def weather_fetch(city_name):
    """
    Fetch current temperature and humidity for a given city using WeatherAPI.
    """
    WEATHER_API_KEY = "0dce1422df3b419bbf4110853252303"  # Your actual API key
    WEATHER_URL = "https://api.weatherapi.com/v1/current.json?"  # Correct URL for current weather
    
    complete_url = f"{WEATHER_URL}key={WEATHER_API_KEY}&q={city_name}"
    response = requests.get(complete_url)
    data = response.json()

    if response.status_code == 200:
        current_weather = data.get("current", {})
        temperature = current_weather.get("temp_c", 0)  # Current temperature in Celsius
        humidity = current_weather.get("humidity", 0)   # Current humidity percentage
        return temperature, humidity
    else:
        print(f"Error fetching weather data: {data.get('error', {}).get('message', 'Unknown error')}")
        return None


@app.route('/')
def home():
    return render_template('index.html', title="Crop Recommendation")

@app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    """
    Handles crop prediction based on user input.
    """
    if request.method == 'POST':
        try:
            # Get inputs from the user
            N = int(request.form['nitrogen'])
            P = int(request.form['phosphorous'])
            K = int(request.form['pottasium'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])
            city = request.form.get("city")

            # Fetch weather details for the entered city
            weather_data = weather_fetch(city)
            if weather_data:
                temperature, humidity = weather_data

                # Prepare input data for model prediction
                input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

                # Make the crop prediction
                prediction = crop_recommendation_model.predict(input_data)[0]

                # Return a JSON response to the frontend
                return jsonify({
                    'temperature': temperature,
                    'humidity': humidity,
                    'prediction': prediction,
                    'city': city
                })

            else:
                return jsonify({'error': 'City not found'})
        except Exception as e:
            return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
