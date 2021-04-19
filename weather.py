from datetime import datetime
import requests

city_name = input('Enter city name: ')
country_code= input ('Enter country code: ')

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city_name+','+country_code+'&appid=eb2ca2be29f51c799a233f2691ce7736&units=metric')
rj = r.json()

if r.status_code==200:
    lon = rj['coord']['lon']
    lat = rj['coord']['lat']
    description = rj['weather'][0]['description']
    temperature = int(rj['main']['temp'])
    feels_like = int(rj['main']['feels_like'])
    pressure = rj['main']['pressure']
    humidity = rj['main']['humidity']
    sunr = rj['sys']['sunrise']
    suns = rj['sys']['sunset']
    sunrise = datetime.fromtimestamp(sunr).strftime('%H:%M')
    sunset = datetime.fromtimestamp(suns).strftime('%H:%M')

    print('---WEATHER REPORT---')
    print('Coordinates of ', city_name, ' are: lon= ', lon, ' lat= ', lat)
    print('Weather description: '+description )
    print('Temperature is : ', temperature, 'C fells like ', feels_like, 'C')
    print('Sunrise is at: ', sunrise, ' sunset is at: ', sunset)

else:
    print('Please enter valid city and country code.')