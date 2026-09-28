stock = int(input("Stock: "))
requested = int(input("Requested quantity: "))
if requested <= stock:
    print("Order can be fulfilled")
else:
    print("Insufficient stock")
