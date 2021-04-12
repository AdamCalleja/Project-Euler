def is_prime(integer):
    if integer <= 1:
        return False
    if isinstance(integer, int) == False:
        print(integer, "is not an integer. Please input an integer.")
    for potential_factor in range(2, integer):
        if integer % potential_factor == 0:
            return False
    return True 