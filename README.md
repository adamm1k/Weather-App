# Weather App

A simple weather app built with Flask and integrated with the OpenWeatherMap API.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features

- Get current weather information for a specified city.
- Displays temperature in Fahrenheit.
- Clean and modern user interface.

## Requirements

- Python (3.x recommended)
- Flask
- requests

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/weather-app.git
    ```

2. Navigate to the project folder:

    ```bash
    cd weather-app
    ```

3. Install the required dependencies:

    ```bash
    pip install Flask requests
    ```

4. Get your API key from [OpenWeatherMap](https://openweathermap.org/api) and replace `'YOUR_API_KEY'` in `app.py` with your actual API key.

## Usage

1. Run the Flask app:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Enter a city in the form and click "Get Weather" to see the current weather information.

## License

This project is licensed under the [MIT License](LICENSE).

