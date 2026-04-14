import requests


def greet():
    print("\n")
    print("╔══════════════════════════╗")
    print("║  WELCOME TO Weather App  ║")
    print("╚══════════════════════════╝")
    print("\n")


api_key = "bd5e378503939ddaee76f12ad7a97608"

greet()

while True:

    print("\n╔═════════════════════════════════════════════════════╗\n")

    city = input("\t\t  Enter City: ")

    if city == '' or city.isdigit() == True or city == None or city.isspace() == True:
        print('\t\t  please enter valid city name...\n')

        continue

    else:
        break


url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    city_name = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n\t══════════════════════ Details ══════════════════════\n")

    print(f"\t\t [ 1. City - {city_name} |  Country - {country} ]\n")
    print(f"\t\t [ 2. Temprature - {temperature} ]\n")
    print(f"\t\t [ 3. Feels Like - {feels_like} ]\n")
    print(f"\t\t [ 4. Humidity - {humidity} ]\n")
    print(f"\t\t [ 5. Pressure - {pressure} ]\n")
    print(f"\t\t [ 6. Weather - {weather} ]\n")
    print(f"\t\t [ 7. Wind Speed - {wind_speed} ]\n")

else:
    print(f"\t  City - {city} is not found, please try again...\n")

print('╚══════════════════════════X══════════════════════════╝')

