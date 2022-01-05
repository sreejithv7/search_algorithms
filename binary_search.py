
from statistics import median
from math import ceil

value = 9

# binary search
lst = [3,4,5,6,7,8,9,10,11]

mid = ceil(median(range(1, len(lst))))

print(mid)

for el in range(3):
    if el > lst[mid]:
        if el > lst[]


def get_median(min_index, max_index):
    return ((min_index + max_index)/2) + 1
    # return ceil(median(range(1, len(index))))


def check_position(index):
    if value == lst[get_median(index)]:
        print(lst.index(value))
    elif value > lst[get_median(index)]:

        check_position(index)
    elif 
