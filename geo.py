import requests
import datetime
from pprint import pprint


open_weather_token = '4c5a015df3cc9900554218396f639c35'
city = 'London'

def get_weather(city, open_weather_token):

    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json()
        # pprint(data)

        citys = data["name"] # берем из полученных данных название города
        cur_weather = data["main"]["temp"] # берем из полученных данных температуру
        humidity = data["main"]["humidity"] # берем влажность из полученных данных
        pressure = data["main"]["pressure"] # Берем давление из полученных данных
        wind = data["wind"]["speed"] # берем скорость ветра из полученных данных
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]) # время рассвета
        return (f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                f"Погода в городе {citys}\nТемпература: {cur_weather}С\n"
                f"Влажность: {humidity}%\n"
                f"Давление: {pressure} мм.рт.ст\n"
                f"Скорость ветра: {wind}м/с\n"
                f"Восход солнца: {sunrise_timestamp}\n"
                f"Хорошего дня!"
                )
        
        # weather = "Погода в городе {}\n".format(citys)
        # weather += "Температура: {}\n".format(cur_weather)
        # weather += "Влажность: {}\n".format(humidity)
        # return (weather)
        
       

    except Exception as ex:
        print(ex)
        print('Проверьте название города')



# def main():
#     get_weather(city, open_weather_token)



# if __name__ == "__main__":
#     main()

