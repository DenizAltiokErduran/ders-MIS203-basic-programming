correct_password = "basic203"
attempts = 0
while True:
    password = input("enter password: ")
    attempts = attempts + 1
    
    if password ==correct_password:
        print("access granted!")
        break
    elif attempts == 5:
        print("Too many attempts. Account locked.")
        break
    else:
        print(f"Wrong password. {5 - attempts} attempts left.")
