def count11(seq):
    # Define this function and return the number of occurrences as a number
    count = 0
    for i in range(len(seq) - 1):
        if seq[i] == 1 and seq[i+1] == 1:
            count += 1
    return count

print(count11([0, 0, 1, 1, 1, 0,]))     # This should return 2
