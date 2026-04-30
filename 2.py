a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the first number to check for multiples: "))
d = int(input("Enter the second number to check for multiples: "))

numbers = range(a, b+1)
result = filter(lambda x: x % c == 0 and x % d == 0, numbers)
print(sum(result))
