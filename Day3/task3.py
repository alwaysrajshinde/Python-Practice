# Task 3: Prime Number (IMPORTANT)
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2,n):
        if n % i == 0 :
            return False
        
    return True

test1 = is_prime(6)
print(test1)