
sequence = [4,5,3,2,6,4,9,8]
my_list = [4,5,3,2,6,4,9,8]

def selection_sort(sequence):
    smallest = 0
    for i in range(0, len(sequence)-1):
        print('now i: ', i)
        for index, element in enumerate(sequence[i:]):
            if index == 0:
                smallest = element
            elif element < smallest:
                smallest = element
            print(smallest)
        print(f'sequence: {sequence} now for i: {i}')
        # interchange i^th element with the smallest element after index i (as list.index(el) only returns the first occurence of el) 
        sequence[sequence[i:].index(smallest)+i] = sequence[i]
        sequence[i] = smallest
        print(f'sequence: {sequence} now for i: {i}')
    return sequence


print('By first method: ', selection_sort(sequence))


def selection_sort2(my_list):
    for i in range(0, len(my_list)-1):
        min_index = i

        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j

        if min_index != i:
            my_list[min_index], my_list[i] = my_list[i], my_list[min_index]
        
    return my_list

print('By second method: ', selection_sort2(my_list))