a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter a number to check for multiples: "))
d = int(input("Enter a number to check for the last digit: "))
numbers = range(a, b+1)
filtered = map(lambda x: x % 10 == d and x % c != 0, numbers)

print(sum(filtered))
