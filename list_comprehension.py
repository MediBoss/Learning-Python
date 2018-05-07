# Function to return all letters of a string in a list using list comprehension
def list_comprehension(word):
    return [letter for letter in word]

# Function to return all letters of a string in a list using iteration
def iteration(word):
    word_letters = []
    for letter in word:
        word_letters.append(letter)

    return word_letters

print iteration('Programming')
print list_comprehension('Programming')
