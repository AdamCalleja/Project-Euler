primes = []
limit_value = 100 000

# the 'limit_value' variable above holds the highest number that you
# want to check. 

highest_known_prime = 2

# This varible highest_known_prime will be used to determine all of 
# the primes within the given range. 

primes = [True for integer in range(2, limit_value + 1)]

# The above creates a list 'primes' holding the value 'True' for each
# integer from 1 to the limit value. The integer itself can be determined
# from the indieces of the elements. 

while primes[(highest_known_prime - 2): (limit_value + 1)].count(False) < len(primes[(highest_known_prime - 2): (limit_value + 1)]):
    if highest_known_prime == True:
        for multiple in range(2, (limit_value + 1), highest_known_prime):
            primes[multiple - 2] = False

        # The above goes through all of the multiples of the highest_known_prime
        # setting the corresponding value in 'primes' to false (only if
        # highest_known_prime is not a multiple of a previous prime).
        # note: the index 'multiple - 2' is used to account for the fact that 
        #       indexing starts at 0 in Python. 

    highest_known_prime += 1

for potential_prime in primes:
    if potential_prime == True:
        potential_prime = primes.index(potential_prime)
    else:
        primes.pop(potential_prime)

# The above replaces the elements with the value 'True' with the value
# of the corresponding prime number in the list
# of primes and deletes all of the elements with the value 'False'. 

prime_count = len(primes)

print("There are", prime_count, "primes in the given range")