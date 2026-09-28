correct_password = "basic203"
attempts = 0
while True:
    password = input("Enter password: ")
    attempts = attempts + 1
    if password == correct_password:
        print("Access granted!")
        break
    if attempts == 3:
        print("Too many attempts. Account locked.")
        break
    print(f"Wrong password. {3 - attempts} attempts left.")
