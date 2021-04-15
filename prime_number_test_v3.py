import math
## The 'math' library needs to be imported so that the 'sqrt()' and 'floor()' functions
## can be used. 

def is_prime(integer):
    if integer <= 1:
        return False
    if integer == 2:
        return True
    if integer > 2 and integer % 2 == 0: 
        return False
    if float(integer).is_integer() == False:
        print(integer, "is not an integer. Please input an integer.")
        return
    max_divisor = math.floor(math.sqrt(integer))
    for potential_factor in range(2, (max_divisor + 1)):
        if integer % potential_factor == 0:
            return False
    return True 

## This function has been made more efficient than the previous version by instantly returning
## false if the integer is even. Since all even numbers (apart from 2) are composite, there is no 
## need to check if these numbers have divisors. This makes the function more efficient since it 
## does not iterate through the divisors of the even numbers. 

