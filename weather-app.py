from flask import Flask
import os
import requests

app = Flask(__name__)

@app.route("/weather")
def weather():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    city = "Vladimir"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return f"Ошибка: {data.get('message', 'не удалось получить данные')}"

        city_name = data["name"]
        temp = round(data["main"]["temp"])
        description = data["weather"][0]["description"]

        # Возвращаем обычный понятный текст
        return f"Город: {city_name}\nТемпература: {temp}°C\nПогода: {description}"

    except Exception as e:
        return f"Ошибка сервера: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)