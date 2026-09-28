start = int(input("Countdown from: "))
total = 0
while start > 0:
    print(start)
    total = total + start
    start = start - 1
print("Liftoff!")
print("Sum of numbers: " + str(total))
