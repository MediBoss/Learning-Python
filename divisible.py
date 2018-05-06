
# Function to find all the numbers that are divisble by the parameter

def list_of_divisble_numbers(number_argument):
    for num in range(1,number_argument + 1):
        if number_argument % num == 0:
            print num
# Function to tell wheater a number is even or odd
def is_num_even_or_odd(number_argument):
    if number_argument % 2 == 0:
        print number_argument," is even"
    elif number_argument % 2 != 0:
        print number_argument, " is odd"
    else:
        print "Invalid number"
