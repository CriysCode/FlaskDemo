from flask import Flask, render_template, request, redirect, url_for
import requests
import json
from flask_sqlalchemy import SQLAlchemy
from script_py import farenheit_to_celsius

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST',])
def index():
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=517a5836c67575144f26a604751ce2d9'
    
    city = 'Sydney'
    #generate a 200 response code from openweatherapi
    
    
    r = requests.get(url.format(city)).json()
    
    weather = {
        #search thrugh endpoint dictionary to find the data you want
        'city' : city,
        'temp' : r['main']['temp'], 
        'description' : r['weather'][0]['description'],  
        'icon' : r['weather'][0]['icon'],
        'feels_like' : r['main']['feels_like']
    }   
    #get temp
    farenheit = weather['temp']
    celcius = farenheit_to_celsius(farenheit)
    feels_like_kelvin = weather['feels_like']
    feels_like_celcius = farenheit_to_celsius(feels_like_kelvin)
    #convert temp to celcius
    return render_template('weather.html', response=r, weather=weather , temperature_celcius=celcius, feels_like_cel=feels_like_celcius)

if __name__ == '__main__':
    app.run(debug=True)