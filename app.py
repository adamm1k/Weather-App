from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with  your API KEY
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')

    if not city:
        return render_template('index.html', error='Please enter a city.')

    params = {'q': city, 'appid': API_KEY, 'units': 'imperial'}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
        }
        return render_template('index.html', weather=weather_info)
    else:
        error_message = f"Error: {data['message']}"
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
