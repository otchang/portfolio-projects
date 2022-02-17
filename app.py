from weather_pkg.weather_module import get_weather, print_random_msg, get_city_coords

'''
    This program calls openweather's apis (One call & Geocode), grabs the api's json data, accesses it to grab
    the temperature and weather, converts to F/C and warns the user what the weather conditions are in the destination city
'''

random_msg_safe = ['You get the green light to travel!', 'Its looking pretty good out there!', 'Try not to have too much fun out there!']
random_msg_notSafe = ['Its looking dangerous to fly out there!','Not looking safe to travel!', 'Not advised to travel!']

mild_weather_list = [300,301,302,310,311,312,313,321,500,501,520,521,800,801,802,803,804]
extreme_weather_list = [
                        200,201,202,210,211,212,221,230,
                        231,232,314,502,503,504,511,521,
                        522,531,600,601,602,611,612,613,
                        615,616,620,621,622,701,711,721,
                        731,741,751,761,762,771,781
                        ]

# All 8xx clouds
# List of extreme weather ids:
#   741, 711, 701, 762, 721: fog, smoke, mist, ash, haze
#   All 6xx snow
#   531, 522, 521, 511, 504, 503, 502, 501: ragged shower rain, heavy intensity shower rain, shower rain, freezing rain, extreme rain, very heavy rain, heavy intensity rain, moderate rain
#   321, 314, 313, 312, 302: shower drizzle, heavy shower rain and drizzle, shower rain and drizzle, heavy intensity drizzle rain, heavy intensity drizzle
#   All 2xx thunderstorm


while True:
    print("\nWelcome to Weather Advisor!")
    
    while True:
        city = input("\nWhat city do you want to travel to? ")

        if city == '' or city.isdigit() == True:
            print("Error: Type in a city name.")
            continue
        
        print(f"1 | Get today's weather for {city}")
        print(f"2 | Get tomorrow's weather for {city}")
        print("3 | Choose another city")
        print("4 | Quit")
        choice = input("Choose an option: ")
        if choice == '':
            print("Error: Choose a valid option.")
        if choice == '1':
            weather_list = get_weather(get_city_coords(city), city)
            weather_id = weather_list[0]               
            daily_weather = weather_list[1]             
            print(f"Weather: {daily_weather}.")

            if weather_id in mild_weather_list:
                print_random_msg(random_msg_safe)
            elif weather_id in extreme_weather_list:
                print_random_msg(random_msg_notSafe)
        elif choice == '2':
            weather_list = get_weather(get_city_coords(city), city)
            weather_id = weather_list[0]
            daily_weather = weather_list[1]
            print(f"Weather: {daily_weather}.")

            # determine whether to advise to travel or not
            if weather_id in mild_weather_list:
                print_random_msg(random_msg_safe)
            elif weather_id in extreme_weather_list:
                print_random_msg(random_msg_notSafe)
        elif choice == '3':
            continue
        elif choice == '4':
            break
    break
            

