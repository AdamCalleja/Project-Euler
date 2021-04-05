import prime_number_test
## Imported a module containing a function to test whether an input is prime. 

prime_number_counter = 1
iterator = 1 

while prime_number_counter != 10001:
    iterator += 2
    print(iterator)
    if prime_number_test.is_prime(iterator) == True:
        prime_number_counter += 1

print(iterator)



