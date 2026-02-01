# Task 3: Larger Number

def larger_number(a,b):
    if a == b :
        return "Equal"
    elif a > b : 
        return a
    elif b > a :
        return b

task1 = larger_number(10,20)
print(task1)

task2 = larger_number(5,5)
print(task2)