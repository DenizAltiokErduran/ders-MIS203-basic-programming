amount = float(input("Order amount: "))
print("Over free-delivery threshold:", amount >= 500)
print("Exactly at threshold:", amount == 500)
print("Below threshold:", amount < 500)
