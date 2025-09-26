#Count the frequency of each character in a string using a dictionary.


Text = input("Enter the text : ")

frequency = {}

for char in Text:
    if char in frequency:
        frequency[char] += 1

    else:
        frequency[char] = 1

print("Character frequencies:")
for key, value in frequency.items():
    print(f"{key}: {value}")


#Output is 
#Enter the text : banana
#Character frequencies:
#b: 1
#a: 3
#n: 2