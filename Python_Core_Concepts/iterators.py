
import operator
import itertools # the module that contains the functions



def main():

    list_one = [1,4,5,7,9,12]
    list_two = ['Janet', 'Christian', 'Elliot', 'Medi', 'Yves']

    '''
    Function 1 : accumulate() - Takes an iterator and function,
                 return the result in a iterator

    '''
    result_one = itertools.accumulate(list_one, operator.mul)
    result_two = itertools.accumulate(list_one, max)

    #print(result_one)
    #print(result_two)

    '''
    Function 2 : combinations() - Takes an iterator and integer,
        return all unique combination that have the integer member

    '''

    result_three = itertools.combinations(list_two, 2)
    for each in result_three:
        pass
        #print(each)

    '''
    Function 3 : count(start=0, step=1) - Makes an iterator that returns
    step spaced values starting from start.

    '''

    for i in itertools.count(10,2):
        print(i) 
        if i > 20:
            break



if __name__ == "__main__":
    main()
