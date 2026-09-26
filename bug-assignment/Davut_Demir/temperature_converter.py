count = 0
while True:
    text = input("Enter temperature in Celsius (x to quit): ")
    if text == "x":
        break
    celsius = float(text)
    fahrenheit = celsius * 9 / 5 + 32
    count = count + 1
    print(f"{celsius} C = {fahrenheit} F")
print(f"You converted {count} temperatures.")
