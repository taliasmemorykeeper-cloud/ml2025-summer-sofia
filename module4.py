N = int(input("How many numbers do you want to enter?"))
numbers = []

for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

X = int(input("Which number do you want to find? "))

if X in numbers:
    print(numbers.index(X) + 1)
else:
    print(-1)