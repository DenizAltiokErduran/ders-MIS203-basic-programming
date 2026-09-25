correct_password = "mis2026"
attempts = 0
while True:
    password = input("Enter password: ")
    attempts = attempts + 1#stringle bir şeyi toplayamayız
    if password == correct_password:
        print("Access granted!")#tırnak işareti yok
        break
    if attempts >= 5:#eşittir olmadığı için 6 hak veriyordu
        print("Too many attempts. Account locked.")
        break
    print(f"Wrong password. {5 - attempts} attempts left.")
