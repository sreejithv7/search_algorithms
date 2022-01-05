
test_sequence = [4,5,3,2,6,4,9,8]


def bubble(sequence):
    for i in range(0, len(sequence)):
        for j in range(1,len(sequence)-i):
            if sequence[j-1] > sequence[j]:
                sequence[j], sequence[j-1] = sequence[j-1], sequence[j]
    return sequence

print(bubble(test_sequence))


def bubble_sort(sequence):
    for i in range(len(sequence)-1, 0, -1):
        for j in range(i):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
    return sequence

print(bubble_sort(test_sequence))
