# Task 4: Count Even Numbers in a List

def count_of_even_nums(num_list):
    count = 0
    for i in num_list:
        if i % 2 == 0 :
            count += 1
    return count

test = count_of_even_nums([2, 5, 6, 9, 10])
print(test)