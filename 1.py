line = input("Enter text: ")
i = int(input("Enter the first number: ")) - 1
j = int(input("Enter the second number: ")) - 1
needed_line = line[i:j+1]
result = filter(lambda x: x!=x.lower(), needed_line)

print("Number of uppercase characters:",len(list(result)))
