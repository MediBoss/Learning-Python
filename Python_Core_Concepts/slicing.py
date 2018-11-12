
""" 
Slicing helps us to get sub elements of an iterable object without crazy loops
"""
    list_one = [1,2,3,4,5,6,7,8,9,10]

    answer_one = list_one[1:4] # gets elements from 1st to 5th index exclusive

    # gets all even numbers from 1st to 8th elementself.
    # :2 tells python to increment by 2
    answer_two = list_one[1:7:2]

    # get list backward
    backward_list = list_one[::-1]
