# Task 2: Sum of numbers

def sum_of_numbers(n):
    total = 0
    for i in range(1,n+1):
        total += i

    return total

test1 = sum_of_numbers(5)
print(test1)

test2 = sum_of_numbers(10)
print(test2)
