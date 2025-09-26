# Find the maximum element in a list without using built-in functions.

def max_num(lst):
    maximum = lst[0]
    
    for num in lst:
        if num > maximum:
            maximum = num
    
    return maximum


numbers = [5, 8, 2, 10, 3, 7]
print("Maximum element:", max_num(numbers))

# or in spimple we do with the use of max function

print("Maximum element:", max(numbers))

#output is
#Maximum element: 10