# Install requests in the terminal before importing the library
# Requests is used to connect to the internet to send and receive information

import requests

# To use this API, sign up at https://openweathermap.org/api to access the API key.
# Replace (api_key) below with your own key.
# This API uses the OpenWeatherMap API to get current weather data based on the user's input. You can exclude or include as many features/parameters as you'd like

api_key = "5b64698ebf48aad2acf480d96990c289"

user = input("Which Country or City are you travelling to? ")

response =  requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user}&units=metric&APPID={api_key}")
data = response.json()

print(data)

country = data["name"]
weather = data["weather"][0]["description"]
temp = round(data["main"]["temp"])
feels_like = round(data["main"]["feels_like"])

def outfit_recommendations(temp):
    if temp >= 30:
        return ["Shorts", "Lightweight T-shirt's", "Sun dresses", "Sandals"]
    elif 20 <= temp < 30:
        return ["Linen trousers", "Maxi Dresses", "Lightweight T-shirt's", "Sandal's"]
    elif 10 <= temp < 20:
        return ["Jeans", "Trouser's", "Cardigan's", "Trainer's", "Shoes"]
    elif temp < 10:
        return ["Winter coat's", "Jumper's", "Hat's", "Scarf's", "Gloves", "Boot's"]
    else:
        return None

outfits = outfit_recommendations(temp)

print(f"Weather type: {weather[:20]}")
print(f"🌤️The weather in {country} is: {temp}°C but feels like {feels_like}°C")
print(f"🧥 Recommended clothing to pack for {country}'s weather:")
for item in outfits:
    print(f"- {item}")

is_warm = temp >= 20
is_ok = temp > 12 < 20


if is_warm:
    print("Oh!, Dont forget your SPF 50, sunglasses & a fan.")
elif is_ok:
    print("Dont forget to bring a light jacket for the evenings, as it can get chilly!")
else:
    print("Wrap up warm, its a little on the cold side!")