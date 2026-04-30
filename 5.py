from functools import reduce
import math

a = int(input("Enter left border a: "))
b = int(input("Enter right border b: "))
c = int(input("Enter number c (multiple check): "))

numbers = range(a, b + 1)

filtered_numbers = filter(
    lambda x: x % c == 0 and math.isqrt(x)**2 == x,
    numbers)


result = reduce(lambda acc, x: acc * x, filtered_numbers, 1)

print("Result: ", result)
