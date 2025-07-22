import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set your OpenWeatherMap API key here
API_KEY = '496a84dcded04da4328e36a7f2b1d2bb'  # Replace with your own API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# List of cities to fetch weather data for
cities = ['Mumbai', 'Delhi', 'Chennai', 'Kolkata', 'Bangalore']

# Function to fetch weather for a city
def fetch_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code == 200 and 'main' in data:
            return {
                'City': city,
                'Temperature (°C)': data['main']['temp'],
                'Humidity (%)': data['main']['humidity'],
                'Pressure (hPa)': data['main']['pressure']
            }
        else:
            print(f"Failed for {city}: {data.get('message', 'No message')}")
            return None
    except Exception as e:
        print(f"Error for {city}: {e}")
        return None

# Fetch data for all cities
weather_list = [fetch_weather(city) for city in cities]
weather_data = [entry for entry in weather_list if entry]

# Convert to DataFrame
df = pd.DataFrame(weather_data)

# Set plot style
sns.set(style="whitegrid")

# Create a dashboard using subplots
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle('Weather Dashboard: Indian Cities', fontsize=16)

# Temperature plot
sns.barplot(data=df, x='City', y='Temperature (°C)', palette='coolwarm', ax=axes[0])
axes[0].set_title('Temperature')

# Humidity plot
sns.barplot(data=df, x='City', y='Humidity (%)', palette='Blues', ax=axes[1])
axes[1].set_title('Humidity')

# Pressure plot
sns.barplot(data=df, x='City', y='Pressure (hPa)', palette='Greens', ax=axes[2])
axes[2].set_title('Pressure')

# Layout adjustment
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()