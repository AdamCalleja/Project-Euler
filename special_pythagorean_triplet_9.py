import math

desired_pythagorean_triplet_sum = 1000
pythagorean_triplet_sum = 0
pythagorean_integer_a = 0

def pythagorean_triplet(integer_a):
    integer_b = 1
    hypotenuse = 1.5
    while hypotenuse.is_integer() == False:
        hypotenuse = math.sqrt((integer_a ** 2) + (integer_b ** 2))
        integer_b += 1
        if hypotenuse + integer_a + integer_b > desired_pythagorean_triplet_sum:
            return []
    return [integer_a, integer_b, hypotenuse]

while pythagorean_triplet_sum != desired_pythagorean_triplet_sum:
    pythagorean_integer_a += 1
    pythagorean_triplet_sum = sum(pythagorean_triplet(pythagorean_integer_a))
    print(sum(pythagorean_triplet(pythagorean_integer_a)))

integer_a = pythagorean_triplet(pythagorean_integer_a)[0]
integer_b = pythagorean_triplet(pythagorean_integer_a)[1]
integer_c = pythagorean_triplet(pythagorean_integer_a)[2]

print(integer_a * integer_b * integer_c)