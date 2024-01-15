import requests

API_KEY = "365b38e0e518d3dba6314b782975cfd4"
def get_deg(deg):
    remain = deg % 360
    deg_dict = {0: 'East', 90: 'North', 180: 'West', 270: 'South'}
    if remain in deg_dict:
        return deg_dict[remain]
    elif remain < 90:
        return "NorthEast"
    elif remain < 180 and remain > 90:
        return "NorthWest"
    elif remain > 180 and remain < 270:
        return "SouthWest"
    elif remain > 270 and remain < 360:
        return "SouthEast"
    
def get_weather():
    """
    function to ask for the city name to make a request.
    """
    city = input("please enter a city: ").lower()
    get_api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY
    return requests.get(get_api).json(), city

def get_info(j, city):
    """
    get the:
    1. temp
    2. feels_like
    3. wind_speed & direction
    """
    print(j)
    print(f"getting information for {city}")
    print(f"temperature in {city} is {round(j['main']['temp'] - 275.15)} °C")
    print(f"wind is {round(j['wind']['speed'] * 3.6, 2)} km/h {get_deg(j['wind']['deg'])}")
    
    
def main():
    json_file, city = get_weather()
    get_info(json_file, city)
    
    
if __name__ == "__main__":
    main()




