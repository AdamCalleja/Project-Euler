primes = []
limit_value = 100000
composite_indices = []
total_popped = 0

# the 'limit_value' variable above holds the highest number that you
# want to check. 

highest_known_prime = 2

# This varible highest_known_prime will be used to determine all of 
# the primes within the given range. 

primes = [True for integer in range(2, limit_value + 1)]

# The above creates a list 'primes' holding the value 'True' for each
# integer from 1 to the limit value. The integer itself can be determined
# from the indieces of the elements. 

unchecked_integers = primes[(highest_known_prime - 2): (limit_value + 1)]
next_multiple_index = (highest_known_prime + highest_known_prime - 2)

## I have declared the varaible above in order to make my code more clean. 

while unchecked_integers.count(False) < len(unchecked_integers):
    if primes[(highest_known_prime - 2)] == True:
        for multiple in range(next_multiple_index, (limit_value - 1), highest_known_prime):
            primes[multiple] = False

        # The above goes through all of the multiples of the highest_known_prime
        # setting the corresponding value in 'primes' to false (only if
        # highest_known_prime is not a multiple of a previous prime).
        # note: the index 'multiple - 2' is used to account for the fact that 
        #       indexing starts at 0 in Python. 

    highest_known_prime += 1
    unchecked_integers = primes[(highest_known_prime - 2): (limit_value + 1)]
    next_multiple_index = (highest_known_prime + highest_known_prime - 2)

for index in range(0, (limit_value - 1)):
    if primes[index] == True:
        primes[index] = index + 2
    else:
        composite_indices.append(index)

for index in composite_indices:
    primes.pop(index - total_popped)
    total_popped += 1

# The above replaces the elements with the value 'True' with the value
# of the corresponding prime number in the list
# of primes and deletes all of the elements with the value 'False'. 

prime_count = len(primes)

print("There are", prime_count, "primes in the given range")