import math
## The 'math' library needs to be imported so that the 'sqrt()' and 'floor()' functions
## can be used. 

def is_prime(integer):
    if integer <= 1:
        return False
    if float(integer).is_integer() == False:
        print(integer, "is not an integer. Please input an integer.")
        return
    max_divisor = math.floor(math.sqrt(integer))
    for potential_factor in range(2, (max_divisor + 1)):
        if integer % potential_factor == 0:
            return False
    return True 

## This function has been made more efficient than the previous version by reducing the number
## of divisors that I have to iterate through. The 'floor()' function is used to get an integer 
## value for the so-called 'mirror line'. 

