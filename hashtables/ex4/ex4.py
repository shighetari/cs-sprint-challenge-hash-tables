def has_negatives(a):
    result = []
    dupes = {}
    # iterate through the array
    for num in a:
        # if we find a negative value make it positive
        if num < 0:
            num = -num
        # put numbers into dupes hash if it's not there (1 means it only appears once)
        if num not in dupes:
            dupes[num] = 1
        # if its already there bump the counter + 1
        else:
            dupes[num] += 1
    # go over dupes
    for key in dupes:
        # if the number appeared more than once (greater than 1), put it into result array
        if dupes[key] > 1:
            result.append(key)
    return result
if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))