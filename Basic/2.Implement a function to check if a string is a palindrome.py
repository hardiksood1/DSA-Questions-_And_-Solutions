#Implement a function to check if a string is a palindrome.

# Palindrome : A palindrome is a word or phrase that reads the same forward and backward (like madam, racecar, level).

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1] ,print(text)


User_Input = input("Enter the Word :")

if is_palindrome(User_Input):
    print("Yes! It's a palindrome ✅")
else:
    print("No! It's not a palindrome ❌")

#Result is 
#Enter the Word :madam
#madam
#Yes! It's a palindrome ✅