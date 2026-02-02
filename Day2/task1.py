# Task 1: Print numbers 1 to n

def num1ToN(n):
    num_list = []
    for i in range(1,n+1):
        num_list.append(i)
    return num_list

test1 = num1ToN(7)
print(test1)

test2 = num1ToN(1)
print(test2)

