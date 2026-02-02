# Task 3: Largest Number in a List


def large_number(num_list):
    large_num = num_list[0]
    for i in num_list:
        if i > large_num:
            large_num = i
    return large_num

test = large_number([12, 45, 7, 89, 23])
print(test)