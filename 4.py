import json
line = input("Enter a list of lists in JSON format: ")
list_of_lists = json.loads(line)

new_lol = sorted(list_of_lists, key=lambda x: x[1], reverse=True)

print("Sorted list: ", new_lol)
