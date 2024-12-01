import requests


class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_data(self, city):
        """Fetches weather data from the API for a given city."""
        try:
            response = requests.get(
                f"{self.base_url}?q={city}&appid={self.api_key}&units=metric"
            )
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred while fetching data for {city}: {http_err}")
        except requests.exceptions.ConnectionError:
            print("Network error. Please check your internet connection.")
        except requests.exceptions.Timeout:
            print("The request timed out. Please try again later.")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")
        return None

    def parse_weather_data(self, data):
        """Parses weather data and returns a formatted dictionary."""
        if data and data['cod'] == 200:
            weather_info = {
                "city": data['name'],
                "temperature": data['main']['temp'],
                "description": data['weather'][0]['description'],
                "humidity": data['main']['humidity'],
                "wind_speed": data['wind']['speed'],
                "feels_like": data['main']['feels_like'],
                "pressure": data['main']['pressure']
            }
            return weather_info
        else:
            print("Failed to parse data. The city may not exist or the data may be incomplete.")
            return None

    def display_weather(self, weather_info):
        """Displays weather information in a readable format."""
        if weather_info:
            print("\n" + "-" * 30)
            print(f"Weather in {weather_info['city']}:")
            print(f"Temperature: {weather_info['temperature']}°C")
            print(f"Feels Like: {weather_info['feels_like']}°C")
            print(f"Description: {weather_info['description'].capitalize()}")
            print(f"Humidity: {weather_info['humidity']}%")
            print(f"Wind Speed: {weather_info['wind_speed']} m/s")
            print(f"Pressure: {weather_info['pressure']} hPa")
            print("-" * 30)
        else:
            print("No weather information available to display.")

    def run(self):
        """Main method to run the weather app."""
        print("Welcome to the Weather App!")
        while True:
            city = input("\nEnter the city name (or type 'exit' to quit): ").strip()
            if city.lower() == 'exit':
                print("Exiting the Weather App. Have a great day!")
                break

            if not city:
                print("Invalid input. Please enter a valid city name.")
                continue

            data = self.get_weather_data(city)
            weather_info = self.parse_weather_data(data)
            self.display_weather(weather_info)


api_key = "ee43d0195215301ffbcc0d89f67bd6ff"

weather_app = WeatherApp(api_key)

weather_app.run()

