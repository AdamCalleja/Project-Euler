first_100_natural_numbers = [integer for integer in range(1, 101)]
squares_of_first_100_natural_numbers = [integer ** 2 for integer in range(1, 101)]
sum_of_first_100_natural_numbers = sum(first_100_natural_numbers)
sum_of_squares = sum(squares_of_first_100_natural_numbers)
square_of_sum = sum_of_first_100_natural_numbers ** 2

difference = square_of_sum - sum_of_squares