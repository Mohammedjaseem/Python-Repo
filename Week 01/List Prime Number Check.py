## Your code should check if each number in the list is a prime number
from tabnanny import check


check_prime = [26, 39, 51, 53, 57, 79, 85]

for i in range(len(check_prime)):
    if check_prime[i]%2 != 0:
        print(check_prime[i], "is a prime number")  
    else:
        print(check_prime[i], "is not a prime number,because 2 is the factor of it")
