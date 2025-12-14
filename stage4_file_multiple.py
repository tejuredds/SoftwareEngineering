# Stage 4: Read multiple sets from file

print("Weather Modeling (Multiple Inputs)\n")

with open("input_multiple.txt", "r") as file:
    for line in file:
        a, b, c, t = map(float, line.split())
        temperature = a*t*t + b*t + c
        print(f"a={a}, b={b}, c={c}, t={t} → Temperature = {temperature} °C")
