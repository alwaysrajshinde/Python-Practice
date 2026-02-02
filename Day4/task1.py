# Task 1: Reverse a String

def reverse_string(user_string):
    reversed_String = ''
    for i in reversed(user_string):
        reversed_String += i
    
    return reversed_String

test1 = reverse_string("automation")
print(test1)


test2 = reverse_string("abc")
print(test2)