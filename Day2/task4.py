# Task 4: Numbers divisible by 3

def divisible_by_3(n):
    nums_divisible_by_3 = []
    for i in range(1,n+1):
        if i % 3 == 0:
            nums_divisible_by_3.append(i)

    return nums_divisible_by_3

test1 = divisible_by_3(10)
print(test1)

test2 = divisible_by_3(20)
print(test2)