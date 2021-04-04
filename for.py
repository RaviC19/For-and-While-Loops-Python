# The first way I solved this
numbers = [11, 13, 15, 17, 19]

x = 0

for value in numbers:
    x = x+value

print("the sum is", x)

# Solution Using a Conditional
# This solution loops over all the numbers between 10 and 20, checking to see if the number is even inside the loop.

x = 0

for n in range(10, 21):
    if n % 2 == 1:
        x += n

print(x)

# Solution using range step
# Instead of looping over every number between 10 and 20, this solution only loops over the odd numbers.
# Remember, the 3rd argument to range() is the STEP or interval that you want the range to increment by

x = 0

for n in range(11, 21, 2):
    x += n

print(x)
