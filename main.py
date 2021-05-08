from flask import Flask
import requests
from flask import request

# токен с openweathermap
APP_ID = '6e60a433461054c8f2ca8a1d6cb65ad7'

app = Flask(__name__)

# Извлекает данные о погоде и конвертирует из Кельвина в Цельсий
def parse_weather(data):
    try:
        temp = data['main']['temp']
        return f'The temperature is: {float(temp)-273.15:.1f}°'

    except Exception as e:
        return f'Data error: {e}'

# Получить данные о погоде через API
def get_weather(city):
    try:
        r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&amp;appid={APP_ID}')
        if r.status_code != 200:
            return f'Invalid response code: {r.status_code}'
        else:
            return parse_weather(r.json())

    except Exception as e:
        return f'API error: {e}'

# Выводит сведения о погоде в выбранном городе
@app.route("/")
def weather():
    city = request.args.get('city', 'Sankt-Peterburg')
    return get_weather(city)


@app.route("/")
def index():
    return "Welcome! The service takes a date and gives corresponding day of the week"

if __name__ == "__main__":
    app.run()