count = 0
while True:
    text = input("Enter temperature in Celsius (q to quit): ")
    if text == "q" :
        break
    celsius = float(text)
    fahrenheit = celsius * 9 / 5 + 32
    count = count + 1
    print(f"{celsius} C = {fahrenheit} F")
print(f"You converted {count} temperatures.")
