# define a function that will give an output of the GCD of 2 positive integers 'a' and 'b'
def greatest_common_divisor(a, b):
    # using a conditional statement to see if 'a' is less than 'b'
    if a < b:
        # swapping the values of a and b
        a, b = b, a
    # using a while loop to perform a repeated operation
    while b > 0:
        # using the modulus operator to get the remainder
        Remainder = a % b
        a = b
        b = Remainder
    return a
# printing the results by picking random positive integers to get the GCD
print(greatest_common_divisor(4,8))