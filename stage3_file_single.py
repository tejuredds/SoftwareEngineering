# Stage 3: Read from file (single set)

with open("input_single.txt", "r") as file:
    data = file.read().split()

a = float(data[0])
b = float(data[1])
c = float(data[2])
t = float(data[3])

temperature = a*t*t + b*t + c

print("Weather Modeling (File - Single Input)")
print(f"Temperature at time {t} hours = {temperature} °C")
