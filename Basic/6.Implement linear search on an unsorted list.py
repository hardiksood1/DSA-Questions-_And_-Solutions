#Implement linear search on an unsorted list.

my_list = [10, 25, 30, 15, 50, 40]

# Take input from user for the element to search
target = int(input("Enter the element to search: "))

# Initialize a flag to check if element is found
found = False

for index, value in enumerate(my_list):
    if value == target:
        print(f"Element {target} found at index {index}")
        found = True
        break

if not found:
    print(f"Element {target} not found in the list")