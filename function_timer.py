## This python module is designed to help test the efficiency of a function. 
## This is done by timing the function, allowing you to compare the relative 
## times of different versions of the same function. 

## HOW TO USE: Import the module containing the function you want to test. 
##             Call the function below. 
##             Run this module. 

import time

import sieve_of_eratosthenes
## Import the functions that you would like to test above. 

initial_time = time.time()
## This variable holds the time before the funciton is called. 

## --------------------------------------------------

## Call the function that you would like to test here. 

prime_count = len(sieve_of_eratosthenes.main(100000))

print("There are", prime_count, "primes before 100 000")

## --------------------------------------------------

final_time = time.time()
## This varaible holds the time after the function has completed its calculation. 

required_time = final_time - initial_time
## The time taken for the function to run can be calculated by subtracting the 
## final_time from the initial_time. 

print("Time required:", required_time)