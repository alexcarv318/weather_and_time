from django.shortcuts import render
from .scripts.weather_algoritm import current_weather_response, weather_forecast_in_my_location, get_info_by_ip

data = get_info_by_ip()

def index(request):
    main = current_weather_response()
    temp = str(main.get('main').get('temp'))[0:2] + '°C'
    weather = str(main.get('weather')[0].get('main'))
    context = {'temp': temp, 'weather': weather}
    return render(request, 'main/index.html', context)

def forecast(request):
    weather_main = current_weather_response()
    weather = str(weather_main.get('weather')[0].get('main'))

    location = data.get('City')

    main = weather_forecast_in_my_location(location)
    info = []
    for i in range(0, len(main[0]), 2):
        temp = f'{int(main[1][i])}°C / {int(main[1][i+1]) + 3}°C'
        dictionary = {'date': main[0][i][:10], 'weather': main[2][i], 'temperature': temp}
        info.append(dictionary)

    context = {
        'info': info,
        'weather': weather,
    }

    return render(request, 'main/forecast.html', context)