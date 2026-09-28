total = 0
count = 0
while True:
    price = float(input("Enter item price (0 to finish): "))
    if price == 0:
        break
    total = total + price
    count = count + 1

if total > 250:
    discount = total * 15 / 100
else:
    discount = 0

print(f"Items: {count}")
print(f"Total: {total:.2f}")
print(f"Discount: {discount:.2f}")
print(f"To pay: {total - discount:.2f}")
