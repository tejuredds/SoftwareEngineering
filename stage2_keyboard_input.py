# Stage 2: Keyboard Input

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
t = float(input("Enter time (hours): "))

temperature = a*t*t + b*t + c

print("\nWeather Modeling (Keyboard Input)")
print(f"Temperature at time {t} hours = {temperature} °C")
