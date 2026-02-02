# Task 4: Count Vowels

def count_vowels(long_sentance):
    count = 0
    for s in long_sentance.lower():
        if s in "aeiou":
            count += 1
    
    return count        

test1 = count_vowels("automation")
print(test1)

test2 = count_vowels("PYTHON")
print(test2)