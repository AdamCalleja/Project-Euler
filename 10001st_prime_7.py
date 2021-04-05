import prime_number_test
## Imported a module containing a function to test whether an input is prime. 

prime_number_counter = 0
iterator = 0 

while prime_number_counter != 10001:
    iterator += 1
    print(iterator)
    if prime_number_test.is_prime(iterator) == True:
        prime_number_counter += 1

print(iterator)



