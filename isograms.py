"""An isogram is a word that has no repeating letters,
consecutive or non-consecutive. Implement a function
that determines whether a string that contains only
letters is an isogram. Assume the empty string is an
isogram. Ignore letter case."""


def is_isogram(string):
    string = string.lower()  # converts string into lowercase
    letter_list = []  # list for letters
    for letter in string:  # for each letter in the string
        if letter in letter_list:  # checks if the letter is in the list
            return False  # if letter is already in the list, returns False
        letter_list.append(letter)  # if letter is not yet in the list, appends
    return True  # if all letters are checked and not repeating, returns True



print(is_isogram("banana"))
print(is_isogram("Grapes"))
print(is_isogram("aPple"))



