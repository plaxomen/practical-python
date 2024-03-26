# bounce.py
#
# Exercise 1.5

# we have a starting height of 100 meters, referred to as drop_height
# each time the ball bounces from a drop_height the bounce height is equal to (3/5) of drop_height
# print a table showing the height of the first 10 bounces.

bounce_ratio = 3 / 5
bounce_height = 100
for b in range(1, 11):
    bounce_height = bounce_height * bounce_ratio
    print(f"{b} {round(bounce_height, 4)}")
