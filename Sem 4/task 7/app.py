from flask import Flask, render_template
import requests

app = Flask(__name__)

NASA_API = "Ob2JBkQkBl4UKoML73KPHwgTR1XnmgZtefSZQfnX"
URL = f"https://api.nasa.gov/insight_weather/?api_key={NASA_API}&feedtype=json&ver=1.0"

@app.route('/', methods=['GET'])
def index():
    response = requests.get(URL)
    data = response.json()
    
    sol_keys = data.get('sol_keys', [])
    weather_data = {sol: data[sol] for sol in sol_keys}

    return render_template('index.html', weather_data=weather_data)


@app.route('/display', methods=['GET'])
def display():
    return ['Ahmad', 'Malik', 'PAI', 'Lab7']


if __name__ == '__main__':
    app.run(debug=True)
