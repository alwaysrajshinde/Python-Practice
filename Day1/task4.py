# Task 4: Number Type

def numType(n):
    if n > 0 :
        return "Positive"
    
    elif n < 0 :
        return "Negative"

    else:
        return "Zero"

test1 = numType(10)
print(test1)
    
test2 = numType(-3)
print(test2)

test3 = numType(0)
print(test3)