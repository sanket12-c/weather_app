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
