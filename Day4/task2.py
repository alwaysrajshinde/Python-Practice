# Task 2: Palindrome Check (String)

def palindrome_check(user_string):
    reversed_String = ''
    for i in reversed(user_string):
        reversed_String += i
    
    if reversed_String == user_string:
        return True
    else:
        return False

test1 = palindrome_check("madam")
print(test1)

test2 = palindrome_check("python")
print(test2)