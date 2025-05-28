# Outfit Recommender Python Project
In this project, i have created an outfit packer recommender which allows people to find the current weather in the location they will be travelling to and recommends the type of clothing and accessories they should pack for their trip.

## Requests Library📚
- Install requests in the terminal before importing the library
- Requests is used to connect to the internet to access information

## Open Weather API☀️

- To use this API, sign up at https://openweathermap.org/api to access the API key.
- Documentation provided the solution on how to call the api by using requests.get with the following endpoint. >"https://api.openweathermap.org/data/2.5/weather?q={user}&units=metric&APPID={api_key}<
- create an api_key variable with the api key provided by the website such as: >api_key = "5b64698ebf48aad2acf480d96990c289"<
- finally, save the response under the variable data
- This API uses the OpenWeatherMap API to get current weather data based on the user's input. You can exclude or include as many parameters as you'd like to use in your project

