def is_prime(integer):
    if integer <= 1:
        return False
    if isinstance(integer, int) == False:
        print(integer, "is not an integer. Please input an integer.")
    for potential_factor in range(2, integer):
        if integer % potential_factor == 0:
            return False
    return True 

## note: This is the most inefficient function to test if a number is a prime number. 
##       The time taken for this function to find all the prime numbers less than 100 000 was 
##       75.5 s (to 3 s.f.).