# define a function that will give an output of the GCD of 2 positive integers 'a' and 'b'
def finding_greatest_common_divisor(a, b):
    # using a conditional statement to see if 'a' is less than 'b' is true
    if a < b:
        # swapping the values of a and b
        a, b = b, a
    # using a while loop to perform a repeated operation so to get the values of 'a' and 'b' as many times as we want
    while b > 0:
        # using the modulus operator to get the remainder
        Remainder = a % b
        a = b
        b = Remainder
    return a


# display a message to get the application to accept input numbers
message1 = int(input("Enter a number:"))
message2 = int(input("Enter a second number:"))

# displaying an error message if the user inputs a negative number
if message1 < 0 or message2 < 0:
    raise ValueError("Error, enter positive number.")

# call the function, use message1 and message2 as the argument to display the results of the numbers picked by the user
(print(finding_greatest_common_divisor(message1, message2)))
