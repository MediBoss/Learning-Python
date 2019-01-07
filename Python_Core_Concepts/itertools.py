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

    for i in itertools.count(10,3):
        #print(i) if i % 2 == 0 else 0
        if i > 20:
            break

    '''
    Function 4 : chain(*iterables) - Takes many iterables and
        returns a combination of them all.
    '''

    for i in itertools.chain(list_one, list_two):
        pass
        #print(i)

    '''
    Function 5 : groupby(iterables=, key=None) - Groups each like elements in
    its own list within a nested list.

    '''

    data1 = [100,90,80,80,20,100,76,68, 90]
    sorted_data1 = sorted(data1)

    keys = [] # will contain all types1
    groups = [] # will contain all grouped like data within a list

    for k,g in itertools.groupby(sorted_data1):
        keys.append(k) # append the key values
        groups.append(list(g)) # append the group values

    print('groups : ',groups)
    print('keys : ',keys)

    # count the apperence of each element
    count_per_group = [len(i) for i in groups]
    print(count_per_group)

    # combines each element with its count
    zipped_values = dict(zip(keys, count_per_group))
    print(zipped_values)


if __name__ == "__main__":
    main()
