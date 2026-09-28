count = int(input("How many grades? "))
total = 0
i = 0
while i < count:
    grade = float(input(f"Grade {i + 1}: "))
    total = total + grade
    i = i + 1
average = total / count
print(f"Average: {average:.2f}")
if average >= 60:
    print("Result: PASSED")
else:
    print("Result: FAILED")
