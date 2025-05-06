# Crop_recommendation_system
________________________________________
🌾 Crop Recommendation System
A Flask-based web application that recommends the most suitable crop to grow based on user inputs such as nitrogen, phosphorous, potassium levels, pH, rainfall, and live weather data (temperature and humidity) fetched using a weather API.
________________________________________
🚀 Features
•	Predicts the best crop to cultivate based on soil and environmental conditions.
•	Integrates live weather API to fetch temperature and humidity.
•	Trained using a Random Forest Classifier.
•	Simple and interactive web interface using Flask.
________________________________________
📁 Project Structure
Crop Recommendation System/
│
├── app.py                   # Main Flask application
├── RandomForest.pkl         # Trained ML model
├── templates/
│   └── index.html           # Frontend page
├── static/                  # CSS/JS (if any)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
________________________________________
⚙️ Dependencies
Install the following packages before running the app:
Flask
numpy
pandas
scikit-learn
requests
Or install all at once using:
pip install -r requirements.txt
________________________________________
🧪 Steps to Run the Project
💡 Tip: Make sure you have Python and Anaconda installed.
1.	Open Anaconda Prompt.
2.	Navigate to the project directory:
3.	cd path\to\your\project
4.	(Optional) Create a virtual environment:
1.	conda create -n crop_env python=3.10
2.	conda activate crop_env
5.	Install dependencies:
6.	pip install -r requirements.txt
7.	Run the app:
8.	python app.py
9.	Open browser and go to:
http://127.0.0.1:5000
________________________________________
🔑 Notes
•	Ensure the RandomForest.pkl model file is placed in the correct location (update the path in app.py if needed).
•	Replace the placeholder weather API key in app.py with your own valid API key from WeatherAPI.
•	The project uses temperature in Celsius and humidity from the API to make real-time recommendations.
________________________________________
📌 Example Input
•	Nitrogen (N): 90
•	Phosphorous (P): 42
•	Potassium (K): 43
•	pH: 6.5
•	Rainfall: 120
•	City: Bangalore
________________________________________
📞 Contact
Feel free to reach out for suggestions or queries.

