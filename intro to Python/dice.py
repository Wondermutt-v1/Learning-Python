#
# Simulate rolling 2 dice
# Introduction to Python on Linkedin 2026
#

# TODO: Get two random integers between 1 and 6 (inclusive)
import random

die_1 = random.randint(1,6)
die_2 = random.randint(1,6)

print(f"You have rolled a {die_1} and {die_2} total :{die_1+die_2}")
