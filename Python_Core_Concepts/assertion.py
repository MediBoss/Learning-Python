def congratulate_student(test_score):
    try:
        assert(test_score >= 80)
        return "Congratulations on getting", test_score
    except AssertionError:
        print "Must have a grade greater than 80"

def main():
    print congratulate_student(90)
    print congratulate_student(81)
    print congratulate_student(60)

if __name__ == "__main__":
    main()
