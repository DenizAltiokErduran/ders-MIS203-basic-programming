# Bug 1 Fixed: Converted input to int
count = int(input("How many grades? "))
total = 0
i = 0
while i < count:
    grade = float(input(f"Grade {i + 1}: "))
    total = total + grade
    i = i + 1

average = total / count
print(f"Average: {average:.2f}")

# Bug 2 Fixed: Changed <= to >= for passing
# Bug 3 Fixed: Closed the missing quote
if average >= 50:
    print("Result: PASSED")
else:
    print("Result: FAILED")
