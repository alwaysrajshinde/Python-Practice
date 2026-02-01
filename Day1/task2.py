# Task 2: Divisible by 3 AND 5



def divisibleBy3and5(n):
    if n % 3 == 0 and n % 5 == 0:
        return True
    else:
        return False

test1 = divisibleBy3and5(15)
print(test1)

test2 = divisibleBy3and5(9)
print(test2)


