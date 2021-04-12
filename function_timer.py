## This python module is designed to help test the efficiency of a function. 
## This is done by timing the function, allowing you to compare the relative 
## times of different versions of the same function. 

import time

## Import the functions that you would like to test above. 

initial_time = time.time()
## This variable holds the time before the funciton is called. 

## --------------------------------------------------

## Call the function that you would like to test here. 

## --------------------------------------------------

final_time = time.time()
## This varaible holds the time after the function has completed its calculation. 

required_time = final_time - initial_time
## The time taken for the function to run can be calculated by subtracting the 
## final_time from the initial_time. 

print("Time required:", required_time)