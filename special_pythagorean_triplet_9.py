pythagorean_triplet_sum = 0
initial_integer = 0

def pythagorean_triplet(integer):
    other_integer = 1
    while isinstance((sqrt((integer ** 2) + (other_integer ** 2))), int) == False:
        other_integer += 1
    return [integer, other_integer, (sqrt((integer ** 2) + (other_integer ** 2)))]

while pythagorean_triplet_sum != 1000:
    initial_integer += 1
    pythagorean_triplet_sum = sum(pythagorean_triplet(initial_integer))

integer_a = pythagorean_triplet(initial_integer)[0]
integer_b = pythagorean_triplet(initial_integer)[1]
integer_c = pythagorean_triplet(initial_integer)[2]

print(integer_a * integer_b * integer_c)