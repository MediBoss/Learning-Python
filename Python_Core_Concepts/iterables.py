
import itertools
import operator


def main():

    data = {
        "b": 3,
        "a": 2,
        "c": 2
    }

    # The accumulate function combines an iterable and function

    # mul : multiplies each element to the previous
    result_acc = itertools.accumulate(data, operator.mul)
    for each in result_acc:
        print(each)

    result_max = itertools.accumulate(data.values(), max)
    for each in result_max:
        print(each)



if __name__ == "__main__":
    main()
