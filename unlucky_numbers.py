# Loop through numbers 1-20 (inclusive)
# For 4 and 13, print "x is unlucky"
# For even numbers, print "x is even"
# For odd numbers, print "x is odd"

for n in range(1, 21):
    if n == 4 or n == 13:
        print(f"{n} is unlucky")
    elif n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")


# Slightly cleaner way with less print repetition

for n in range(1, 21):
    if n == 4 or n == 13:
        status = "unlucky"
    elif n % 2 == 0:
        status = "even"
    else:
        status = "odd"
    print(f"{n} is {status}")
