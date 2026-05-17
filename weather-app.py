from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

@app.route("/weather")
def weather():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    city = "Moscow"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    data = requests.get(url).json()

    return jsonify({
        "city": data["name"],
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "version": "v1"
    })

app.run(host="0.0.0.0", port=5000)