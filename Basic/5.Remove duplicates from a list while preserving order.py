#Remove duplicates from a list while preserving order.

my_list = [1, 2, 3, 2, 4, 1, 5]

# Create an empty list to store unique elements
unique_list = []


for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original list:", my_list)
print("List without duplicates:", unique_list)


#output is 
#Original list: [1, 2, 3, 2, 4, 1, 5]
#List without duplicates: [1, 2, 3, 4, 5]