#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json

# Title and Description
print("\nTitle: Calculating the Average Temperature for a City Using User Input\n")
print("Description: This project calculates the average temperature for a given city.\n")

# Ask the user for the name of a city
city = input("Enter the name of a city: ")

# Sign up for a free API key from OpenWeatherMap: https://home.openweathermap.org/users/sign_up
api_key = "your_api_key_here"

# Retrieve the current weather data for the specified city
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the temperature information from the weather data
    data = json.loads(response.text)
    current_temperature = data["main"]["temp"]

    # Calculate the average temperature for the current day
    # For the sake of simplicity, we assume the temperature doesn't change during the day
    average_temperature = current_temperature

    # Display the average temperature to the user
    print(f"\nThe average temperature for {city} today is {average_temperature - 273.15:.2f}°C or {(average_temperature - 273.15) * 9 / 5 + 32:.2f}°F.\n")
else:
    print("\nUnable to retrieve weather data. Please check the city name and try again.\n")


# In[ ]:




