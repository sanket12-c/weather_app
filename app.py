import requests
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

API_KEY = "bd5e378503939ddaee76f12ad7a97608"
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# A simple dict of some states and major cities in India for demonstration
INDIAN_STATES_CITIES = {
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Karnataka": ["Bengaluru", "Mysore", "Mangalore"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
    "Delhi": ["New Delhi"],
    "West Bengal": ["Kolkata", "Howrah"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
    "Rajasthan": ["Jaipur", "Udaipur"],
    # Add more states/cities as needed
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Weather App</title>
<style>
  body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(to bottom, #87ceeb, #f0f9ff);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    color: #333;
  }
  h1 {
    margin-bottom: 1rem;
  }
  form {
    margin-bottom: 2rem;
  }
  input[type=text] {
    padding: 0.5rem 1rem;
    font-size: 1rem;
    border-radius: 24px 0 0 24px;
    border: 1px solid #aaa;
    outline: none;
    width: 250px;
  }
  button {
    padding: 0.5rem 1.5rem;
    font-size: 1rem;
    border: 1px solid #2196f3;
    background-color: #2196f3;
    color: white;
    border-radius: 0 24px 24px 0;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  button:hover {
    background-color: #1769aa;
  }
  .weather-result {
    background: white;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 0 15px rgba(0,0,0,0.1);
    max-width: 380px;
    width: 100%;
    text-align: center;
  }
  .temp {
    font-size: 4rem;
    font-weight: bold;
    margin: 1rem 0;
  }
  .desc {
    font-size: 1.3rem;
    text-transform: capitalize;
    margin-bottom: 1rem;
  }
  .detail {
    font-size: 1rem;
    margin: 0.5rem 0;
  }
  .error {
    color: red;
    font-weight: bold;
    margin-top: 1rem;
  }
</style>
</head>
<body>
<h1>Simple Weather App</h1>
<form id="weather-form">
  <input type="text" id="city" name="city" placeholder="Enter city name" required />
  <button type="submit">Get Weather</button>
</form>
<div id="weather-result" class="weather-result" aria-live="polite" role="region"></div>
<script>
  const form = document.getElementById('weather-form');
  const resultDiv = document.getElementById('weather-result');

form.addEventListener('submit', async e => {
  e.preventDefault();
  const cityInputEl = document.getElementById('city');
  const city = cityInputEl.value.trim();
  if (!city) {
    resultDiv.innerHTML = '<div class="error">Please enter a city name.</div>';
    return;
  }
  resultDiv.textContent = "Loading...";

  try {
    const response = await fetch(`/weather?city=${encodeURIComponent(city)}`);
    if (!response.ok) throw new Error('City not found');
    const data = await response.json();

    resultDiv.innerHTML = `
      <div class="temp">${Math.round(data.temp)}°C</div>
      <div class="desc">${data.description}</div>
      <div class="detail">Humidity: ${data.humidity}%</div>
      <div class="detail">Wind Speed: ${data.wind_speed} m/s</div>
    `;
    // Keep the input value intact explicitly
    cityInputEl.value = city;
  } catch (err) {
    resultDiv.innerHTML = '<div class="error">' + err.message + '</div>';
  }
});
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/weather")
def weather():
    city = request.args.get("city", "")
    if not city:
        return jsonify({"error": "City parameter missing"}), 400

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        res = requests.get(API_URL, params=params, timeout=5)
        res.raise_for_status()
    except requests.RequestException:
        return jsonify({"error": "City not found or API error"}), 404

    data = res.json()
    weather_data = {
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(debug=True)





