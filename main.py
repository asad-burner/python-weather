import requests # Importing request library to make requests to api
import math # Importing math library to round 
import pyfiglet  # Importing pyfiglet for big text output
from colorama import Fore, Style  # Importing colorama for colored text

# api keys. please get your own from the websites "ipinfo.info" and "weatherapi.com"
ipinfo_key = ''
weatherapi_key = ''

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    return ip_data['ip']

# Get public IP
ip = get_public_ip()

# Request IP info
ipinfo_response = requests.get(f"https://api.ipinfo.info/api/{ip}?access_key={ipinfo_key}")

# Get the postal code
postal_code = ipinfo_response.json()['zip'][0:3]

# Get weather data using the postal code
weather_response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={weatherapi_key}&q={postal_code}&aqi=no")

# Parse the weather data
weather_data = weather_response.json()




# Get the temperature in Celsius and Fahrenheit
temp_c = round(weather_data['current']['temp_c'])
temp_f = round(weather_data['current']['temp_f'])

# Determine the color based on the temperature
if temp_c <= 10:
    temp_color = Fore.BLUE  # Cold temperature
elif temp_c <= 25:
    temp_color = Fore.YELLOW  # Moderate temperature
else:
    temp_color = Fore.RED  # Hot temperature

# Weather info display
print ('\n\n')
print(Fore.GREEN + 'WEATHER\n' + Style.RESET_ALL)
# Print the temperature in big letters using pyfiglet with color
print(temp_color + pyfiglet.figlet_format(weather_data['current']['condition']['text']).upper() + Style.RESET_ALL)

# print location name in capital letters, in color
print(temp_color + (weather_data['location']['name'] + ", " + weather_data['location']['country']).upper() + '\n' + Style.RESET_ALL)

# print condition



print(f"- Temperature: {temp_c}°C / {temp_f}°F")
# print temperature

feels_like_c = round(weather_data['current']['feelslike_c'])
feels_like_f = round(weather_data['current']['feelslike_f'])

print(f"- Feels like: {feels_like_c}°C / {feels_like_f}°F")

# print other useful info
print(f"- Wind: {weather_data['current']['wind_kph']} km/h")
print(f"- Humidity: {weather_data['current']['humidity']}%")
print(f"- Pressure: {weather_data['current']['pressure_mb']} mbar")
print(f"- UV Index: {weather_data['current']['uv']}")
print(f"- Visibility: {weather_data['current']['vis_km']} km")
