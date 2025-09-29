#Check if a number is prime using a simple loop.

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


#Output

# Enter a number: 5
# 5 is a prime number