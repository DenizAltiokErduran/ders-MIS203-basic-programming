balance = 750
while True:
    choice = input("d = deposit, w = withdraw, q = quit: ")
    if choice == "q":
        break
    amount = float(input("Amount: "))
    if choice == "d":
        balance = balance + amount
    elif choice == "w":
        if amount > balance:
            print("Not enough money!")
        else:
            balance = balance - amount
    print(f"Balance: {balance:.2f}")
print(f"Final balance: {balance:.2f}")
