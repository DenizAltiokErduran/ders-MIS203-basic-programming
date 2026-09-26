secret = 60
tries = 0
while True:
    guess = int(input("Guess the number (1-100): "))
    tries = tries + 1
    if secret > guess:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You found it in {tries} tries.")
        break
