import random

random_numbers = random.sample(range(0,49), 20)

print(random_numbers)

squared = [i**2 for i in random_numbers]
print(squared)
