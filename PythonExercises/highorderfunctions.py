# from functools import reduce

# Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns
# the largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce()
# function directly?
def max_in_list(number_list):
    return reduce((lambda x, y: x if (x > y) else y), number_list)


# Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
# Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list
# comprehensions.
def map_words(word_list):
    list1 = []
    for x in word_list:
        list1.append(len(x))

    list2 = [len(x) for x in word_list]

    list3 = list(map(lambda x: len(x), word_list))

    return [list1, list2, list3]


# Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
# Use only higher order functions.
def find_longest_word(word_list):
    return reduce((lambda x, y: x if (x > y) else y), map(lambda x: len(x), word_list))


# Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an
# integer n and returns the list of words that are longer than n.
def filter_long_words(word_list, target_len):
    return list(filter(lambda x: len(x) > target_len, word_list))


# Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul"
# , "and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English
# into Swedish. Use the higher order function map() to write a function translate() that takes a list of English words
# and returns a list of Swedish words.
def translate(word_list):
    swede_dict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}
    return list(map(lambda x: swede_dict[x], word_list))


# Implement the higher order functions map(), filter() and reduce().
# (They are built-in but writing them yourself may be a good exercise.)
def map(func, list):
    newlist = []
    for x in list:
        newlist.append(func(x))
    return newlist


def filter(func, list):
    newlist = []
    for x in list:
        if func(x):
            newlist.append(x)
    return newlist


def reduce(func, list):
    returnval = None
    for i in range(len(list) - 1):
        if not returnval:
            returnval = list[i]
        else:
            returnval = func(returnval, list[i])
    return returnval