evens = 0
odds = 0
while True:
    text = input("Enter a number (done to finish): ")
    if text == "done":
        break
    number = int(text)
    if number % 2 == 0:
        evens = evens + 1
    else:
        odds = odds + 1
print(f"Even numbers: {evens}")
print(f"Odd numbers: {odds}")
