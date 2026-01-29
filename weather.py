import random

days = int(input("How many days of weather do you want?"))
print("\nWeather Forecast:\n")

for day in range(1, days + 1):
    temp = random.randint(20, 100)
    if temp < 40:
        print("Buuurrrr so cold")
    elif temp < 70:
        print("Now this is almost perfect... but still a little cold")
    else:
        print("Ok this is too hot... you can never win")
    print(f"Day {day}: {temp}°F")
