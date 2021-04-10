import prime_number_test

prime_number_cap = 2000000

prime_numbers = [integer for integer in range(1, (prime_number_cap + 1)) if prime_number_test.is_prime(integer) == True]

print(sum(prime_numbers))