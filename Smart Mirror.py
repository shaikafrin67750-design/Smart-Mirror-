# Smart Mirror using Python

from datetime import datetime

def smart_mirror():
print("\n==============================")
print("        SMART MIRROR")
print("==============================")

```
# Current date and time
current_time = datetime.now()

print("Date :", current_time.strftime("%d-%m-%Y"))
print("Time :", current_time.strftime("%H:%M:%S"))

# Get weather information
temperature = float(input("Enter temperature (°C): "))
humidity = float(input("Enter humidity (%): "))

print("\n------- WEATHER -------")
print(f"Temperature : {temperature:.1f} °C")
print(f"Humidity    : {humidity:.1f} %")

if temperature >= 35:
    print("Weather Status: Hot")
elif temperature >= 25:
    print("Weather Status: Warm")
elif temperature >= 15:
    print("Weather Status: Pleasant")
else:
    print("Weather Status: Cold")

print("\nHave a nice day! 😊")
```

while True:
print("\n1. Display Smart Mirror")
print("2. Exit")

```
choice = input("Enter your choice: ")

if choice == "1":
    smart_mirror()

elif choice == "2":
    print("Smart Mirror Closed.")
    break

else:
    print("Invalid choice! Please try again.")
```
