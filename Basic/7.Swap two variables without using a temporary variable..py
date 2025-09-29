#Swap two variables without using a temporary variable.
#1. Using Addition and Subtraction

a = 5
b = 10

a = a + b  # a becomes 15
b = a - b  # b becomes 5
a = a - b  # a becomes 10

print("a =", a)
print("b =", b)


#2. Using Multiplication and Division

a = 5
b = 10

a = a * b  # a = 50
b = a / b  # b = 5
a = a / b  # a = 10

print("a =", a)
print("b =", b)


#3. Using XOR (Bitwise Operator)

a = 5
b = 10

a = a ^ b  # XOR
b = a ^ b
a = a ^ b

print("a =", a)
print("b =", b)


#4. Using Python's Tuple Unpacking (Most Pythonic)

a = 5
b = 10

a, b = b, a

print("a =", a)
print("b =", b)


#Output
# a = 10
# b = 5   
# a = 10.0
# b = 5.0 
# a = 10  
# b = 5   
# a = 10  
# b = 5   
