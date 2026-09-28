total = 0
count = 0
while True:
    price = float(input("Enter item price (0 to finish): "))
    if price == 0:
        break
    total = total + price
    count = count + 1

if total > 150:
    discount = total * 20/100
    #yüzde kısmı hatalıydı
else:
    #burada iki nokta yoktu  
    discount = 0

print(f"Items: {count}")
print(f"Total: {total:.2f}")
print(f"Discount: {discount:.2f}")
#discount olmalı (indirim)
print(f"To pay: {total - discount:.2f}")
