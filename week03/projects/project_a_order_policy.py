"""Week 3 project A: apply a transparent retail order policy."""

print("Retail Order Policy")
customer = input("Customer name: ").strip()
amount = float(input("Basket amount: "))
member = input("Member (yes/no): ").strip().lower() == "yes"
destination = input("Destination (local/national): ").strip().lower()

if amount < 0:
    print("Invalid basket amount. No quote can be produced.")
elif destination != "local" and destination != "national":
    print("Invalid destination. Choose local or national.")
else:
    if member and amount >= 1000:
        discount_rate = 0.15
        policy = "Member order of at least 1000 TRY"
    elif member:
        discount_rate = 0.05
        policy = "Member discount"
    elif amount >= 1500:
        discount_rate = 0.10
        policy = "Large order discount"
    else:
        discount_rate = 0.0
        policy = "Standard price"

    discount = amount * discount_rate
    after_discount = amount - discount
    if destination == "local":
        shipping = 0.0 if after_discount >= 500 else 35.0
    else:
        shipping = 0.0 if after_discount >= 1000 else 75.0
    total = after_discount + shipping

    print()
    print("=" * 52)
    print(f"ORDER QUOTE FOR {customer}")
    print("=" * 52)
    print(f"Policy: {policy}")
    print(f"Basket amount:  {amount:9.2f} TRY")
    print(f"Discount:      -{discount:9.2f} TRY")
    print(f"Shipping:       {shipping:9.2f} TRY")
    print(f"Total:          {total:9.2f} TRY")
    print("=" * 52)
