#import prime_number_test
#
#prime_number_cap = 2000000
#
#prime_numbers = [integer for integer in range(1, (prime_number_cap + 1)) if prime_number_test.is_prime(integer) == True]
#
#print(sum(prime_numbers))

import prime_number_test

prime_sum_cap = 2000000
prime_sum = 0
prime_numbers = []
initial_integer = 0

while prime_sum < prime_sum_cap:
    if prime_number_test.is_prime(initial_integer) == True:
        prime_numbers.append(initial_integer)
    initial_integer += 1
    prime_sum = sum(prime_numbers)
    if prime_sum > 2000000:
        prime_numbers = prime_numbers[0: -1]

prime_sum = sum(prime_numbers)

print(prime_sum)