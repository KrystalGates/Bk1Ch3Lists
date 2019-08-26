#Instructions
#Use the following code to create a list of 10 random numbers. Each number will be between 0 and 6.

import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))
#The my_randoms list will now contain random numbers

[1, 3, 1, 2, 4, 2, 5, 4, 2, 5]
#Then iterate a different list of numbers that are sequential from 1 to 10.
print(my_randoms)

#Print a message to the console indicating whether each value of
#`number` is in the `my_randoms` list.

for number in range(1, 6):
    if my_randoms.count(number) > 0:
        print(f"my_randoms list contains {number}")
    else:
        print(f"my_randoms list does not contain {number}")


#Example Output in the Terminal
#my_randoms list contains 0
#my_randoms list does not contain 1
#my_randoms list does not contain 2
#my_randoms list contains 3
#my_randoms list contains 4
#my_randoms list does not contain 5
#NOTE: Each run will produce different output.

