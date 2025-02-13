import requests

API_KEY = "b6b7f62738e438e2b6a786454e3e1e75"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperture = round(data["main"]["temp"] - 273.15, 2)
    
    print("Weather:", weather)
    print("Temperture:", temperture, "celsius")
    

else:
    print("An error occurred.")
    