def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    number_of_arrays = len(arrays)
    dupes = {}
    # array of arrays: go over each array
    for array in arrays:
        # go over values of each nested array
        for num in array:
            # if the value is not in dupes, set it to 1
            if num not in dupes:
                dupes[num] = 1
            # otherwise, already exists in dupes, bump the counter so it should be 2
            else:
                dupes[num] += 1
    for key in dupes:
        # if the number appeared the same amount of times as the length of the arrays, its in all nested arrays.
        if dupes[key] == number_of_arrays:
            result.append(key)
    return result
if __name__ == "__main__":
    arrays = []
    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])
    print(intersection(arrays))