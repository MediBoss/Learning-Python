# Function to return all letters of a string in a list using list comprehension
def list_comprehension(word):
    return [letter for letter in word]
# Function to fillter all test score grater than 80
def filter_score(list):
    return [score for score in list if score > 80]

# Function to return all letters of a string in a list using iteration
def iteration(word):
    word_letters = []
    for letter in word:
        word_letters.append(letter)

    return word_letters

    # Organize the codes in the main function
def main():
    #print list_comprehension('Medi')
    #print iteration('Medi')

    test_scores = [89,45,98,67,90,81,80,83,94,95,87]
    print filter_score(test_scores)

if __name__ == "__main__":
    main()
