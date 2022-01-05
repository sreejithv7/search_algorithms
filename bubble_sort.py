
test_sequence = [4,5,3,2,6,4,9,8]


def bubble(sequence):
    for i in range(0, len(sequence)):
        for j in range(1,len(sequence)-i):
            if sequence[j-1] > sequence[j]:
                sequence[j], sequence[j-1] = sequence[j-1], sequence[j]
    return sequence

print(bubble(test_sequence))