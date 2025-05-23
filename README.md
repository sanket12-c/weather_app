
# Weather App with Animated UI using Python Flask and OpenWeatherMap API

This project is a simple yet visually appealing weather application built with Python and Flask as the backend server, utilizing the OpenWeatherMap API for live weather data. The frontend is an interactive single-page interface that displays weather information with animated icons representing sun, clouds, and rain, making the user experience engaging and delightful.

## Features

- **Live Weather Data:** Retrieves current weather data for any city from OpenWeatherMap using a free API key.
- **Animated Weather Icons:** Displays dynamic and visually attractive animations:
  - 3D-like rotating sun for clear weather.
  - Floating clouds animation for cloudy weather.
  - Rain clouds with animated raindrops for rainy conditions.
- **Responsive and Modern UI:** Clean layout and style with CSS animations, adaptable to different screen sizes.
- **No Page Reloads:** Uses JavaScript Fetch API to request weather data asynchronously without refreshing the page.
- **Error Handling:** Shows user-friendly error messages when city is not found or API errors occur.
- **Accessibility:** ARIA roles and live regions improve accessibility for screen readers.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-flask-app.git
   cd weather-flask-app
   ```

2. Create a Python virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Replace the placeholder API key in `weather_app.py` with your OpenWeatherMap API key:
   ```python
   API_KEY = "your_actual_api_key_here"
   ```

5. Run the Flask application:
   ```bash
   python weather_app.py
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage

- Enter a city name in the input box and click "Get Weather".
- View current temperature, weather description, humidity, wind speed, and see an animated icon that corresponds to the weather condition.
- If the city is invalid or data fetch fails, an error message is shown.

## Technologies Used

- **Backend:** Python, Flask, Requests
- **Frontend:** HTML5, CSS3 (Flexbox, Animations), JavaScript (Fetch API)
- **API:** OpenWeatherMap Current Weather API

## Screenshots

*(Add screenshots of the UI showing sun, cloud, and rain animations with weather data.)*

## License

This project is licensed under the MIT License.

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to open issues or submit pull requests.

---

Enjoy exploring weather conditions with an animated and interactive interface!
