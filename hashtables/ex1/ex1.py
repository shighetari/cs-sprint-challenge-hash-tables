def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
   
    possible_weights = {}
    # dictionary with actual weights as keys and what they need to complete the limit as values
    for num in weights:
        #check weights from input
        if num not in possible_weights:
            # 
            possible_weights[num] = limit - num
    # return possible_weights
    for key in possible_weights:
        # if we have duplicates that add up to the limit
        if possible_weights[key] == key and possible_weights[key] in weights:
            small_index = weights.index(key)
            weights.pop(small_index)
            big_index = weights.index(key) + 1
            return [big_index, small_index]
        if possible_weights[key] in weights:
            big_index = weights.index(possible_weights[key])
            small_index = weights.index(key)
            return [big_index, small_index]



'''
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    string_utf = weights.encode()

    total = 0
    for char in string_utf:
        total += char
    return total % limit 
hash_table = [None] * 8 ##do anything by the power of 2 for good practice 32/64 etc bits op

index = get_indices_of_item_weights(1,2, len(hash_table))
hash_table[index] = 'value of 1 weight'

index = get_indices_of_item_weights(2,2, len(hash_table))
hash_table[index] = 'value of 2 weights'


index = get_indices_of_item_weights(1, 2, len(hash_table))

print(hash_table[index])
print(hash_table)
'''