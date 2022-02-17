import random
import requests

APIkey = '90ebbc6df57d82cce5dade5330c63a05'

'''
    This function prints a random message from either mild_weather_list or extreme_weather_list.

    def print_random_msg(msg_list) -> printed message:

    Parameters
    ----------
    msg_list : list
        msg_list represents a list of messages.

    Returns
    -------
    None
        Prints out a random message from either message list.
'''

def print_random_msg(msg_list):
    msg_index = random.randrange(len(msg_list))
    print(f"\n{msg_list[msg_index]}\n")

'''
    This function grabs city name from user input, and returns a list containing latitude, longitude via Openweathermap API call.

    def get_city_coords() -> list[float, float]:

        Returns
        -------
        list[float,float]
            Returns a list with 2 float values: latitude and longitude
'''

def get_city_coords(city): # do not have to call this in main body, just pass this as an argument into get_weather()
    
    geo_api = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={APIkey}"
    geo_json_data = requests.get(geo_api).json()
    lat = geo_json_data[0]['lat']
    lon = geo_json_data[0]['lon']
    return [lat, lon]

'''
This function passes in lon, lat from get_city_coords().
It will get temperature based on city from JSON data and convert to celsius/farenheit.
Returns C/F in degree format and weather conditions of city.

def get_weather(get_city_coords: function) -> list[int, string]:

    Parameters
    ----------
    get_city_coords : function
        returned list that holds longitude and latitude float values

    Returns
    -------
    list[int, string]
        returns list of weather id (int) and weather (string)
'''

def get_weather(get_city_coords, city):
    
    degree = u"\N{DEGREE SIGN}"
    exclude = "minutely,hourly"
    lat = get_city_coords[0]
    lon = get_city_coords[1]

    ow_api = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={APIkey}"
    json_data = requests.get(ow_api).json()
    current_temp_f = round((json_data['current']['temp'] - 273.15) * 1.8 + 32)
    current_temp_c = round(json_data['current']['temp'] - 273.15)
    # F = (K - 273.15) * 1.8 + 32)
    # C = K - 273.15
    weather_id = json_data['daily'][0]['weather'][0]['id']   
    daily_weather = json_data['daily'][0]['weather'][0]['description']

    if not city.isdigit():
        print(f"\nThe current temperature in {city} is {current_temp_f}{degree}F/{current_temp_c}{degree}C.")
    elif city.isdigit() == True:
        print("Invalid entry.")
        exit()

    return [weather_id, daily_weather]