# Task 3: Sum of even numbers

def sum_of_even_nums(n):
    even_nums = []
    for i in range(1,n+1):
        if i % 2 == 0 :
            even_nums.append(i)
    
    return sum(even_nums)

test1 = sum_of_even_nums(10)
print(test1)

test2 = sum_of_even_nums(7)
print(test2)