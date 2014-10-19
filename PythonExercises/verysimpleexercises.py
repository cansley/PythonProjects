# these exercises come from the web page: http://www.ling.gu.se/~lager/python_exercises.html
import re
# 1 define a function max() that takes two numbers and returns the largest of them.
# Use the if-then-else construct available in Python.
# (Its true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)


def max(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        raise ValueError("Values cannot be equal.")


# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
def maxofthree(num1, num2, num3):
    return max(max(num1, num2), num3)


# Define a function that computes the length of a given list or string.
# (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
def length(obj):
    count = 0
    for x in obj:
        count += 1

    return count


# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
def isvowel(value):
    vowels = ["a", "e", "i", "o", "u"]

    if str.isalpha(str(value)) and len(value) == 1 and str.lower(value) in vowels:
        return True
    else:
        return False


# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
# That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")
# should return the string "tothohisos isos fofunon".
def translate(value):
    result = ""
    for c in value:
        if not isvowel(c) and not str.isspace(c):
            result += c + "o" + c
        else:
            result += c
    return result


# Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers
# in a list of numbers.
# For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
def sum(numlist):
    value = 0
    for x in numlist:
        value += x
    return value


def multiply(numlist):
    value = 1
    for x in numlist:
        value *= x
    return value


# Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am testing") should return the string "gnitset ma I".
def reverse(string):
    value = ""
    for x in range(1, len(string) + 1):
        value += string[x * (-1)]
    return value


# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
# For example, is_palindrome("radar") should return True.
def is_palindrome(string):
    return string == reverse(string)


# Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a,
# and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does,
# but for the sake of the exercise you should pretend Python did not have this operator.)
def is_member(value, list):
    for x in list:
        if value == x:
            return True
    return False


# Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
# False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise,
# you should (also) write it using two nested for-loops.
def overlapping(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False


# Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long,
# consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx".
# (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx".
# For the sake of the exercise you should ignore that the problem can be solved in this manner.)
def generate_n_chars(char, count):
    result = ""
    for x in range(count):
        result += str(char)
    return result


# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
#     *******
def historgram(list1):
    for x in list1:
        print(generate_n_chars("*", x))


# The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three
# numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how
# many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.
def max_in_list(list):
    if len(list) > 2:
        val = None
        for x in range(len(list)):
            val = max_in_list([list[x], val])
        return val
    else:
        if list[1] is None or list[0] > list[1]:
            return list[0]
        else:
            return list[1]


# Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
def map_lengths(wordlist):
    lengths = []
    for x in wordlist:
        lengths.append(len(x))
    return lengths


# Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
def find_longest_word(wordlist):
    lengths = map_lengths(wordlist)
    longestIdx = lengths.index(max_in_list(lengths))
    return wordlist[longestIdx]


# Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
def filter_long_words(wordlist, maxlength):
    return list(filter(lambda x: len(x) > maxlength, wordlist))


# Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a
# lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil",
# "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the
# exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.
def is_palindrome_phrase(phrase):
    rx = re.compile("[a-z]", re.IGNORECASE)
    r = ''.join(rx.findall(phrase)).lower()
    return is_palindrome(r)


# A pangram is a sentence that contains all the letters of the English alphabet at least once, for example:
# The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to
# see if it is a pangram or not.
def is_pangram(phrase):
    rx = re.compile("[a-z]", re.IGNORECASE)
    letters = set(rx.findall(phrase.lower()))
    return len(letters) == 26


# "99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips,
# as it has a very repetitive format which is easy to memorize, and can take a long time to sing.
# The song's simple lyrics are as follows:
#
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall.
#
# The same verse is repeated, each time with one fewer bottle.
# The song is completed when the singer or singers reach zero.
#
# Your task here is write a Python program capable of generating all the verses of the song.
def get_99btls_lyrics(starting_number):
    lyric_template = "%d bottles of beer on the wall, %d bottles of beer.\nTake one down, pass it around, %d bottles of beer on the wall.\n\n"
    finalResult = ""
    for x in range(starting_number, 0, -1):
        finalResult += lyric_template % (x, x, x - 1)
    return finalResult


# Represent a small bilingual lexicon as a Python dictionary in the following fashion
# {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}
# and use it to translate your Christmas cards from English into Swedish.
# That is, write a function translate() that takes a list of English words and returns a list of Swedish words.
def translate_swede(phrase):
    swede_dict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}
    response = ""
    for x in str(phrase).split(" "):
        response += swede_dict[x.lower()] + " "
    return response


# Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it.
# Represent the frequency listing as a Python dictionary.
# Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
def char_freq(phrase):
    freq_dict = {}
    for x in phrase:
        if x not in freq_dict.keys():
            freq_dict[x] = 1
        else:
            freq_dict[x] += 1
    return freq_dict


# In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain text is
# replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 3,
#  A would be replaced by D, B would become E, and so on. The method is named after Julius Caesar,
# who used it to communicate with his generals. ROT-13 ("rotate by 13 places") is a widely used example of a Caesar
# cipher where the shift is 13. In Python, the key for ROT-13 may be represented by means of the following dictionary:
#
# key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
#       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
#       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
#       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
#       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
#       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
#       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
# Your task in this exercise is to implement an encoder/decoder of ROT-13. Once you're done, you will be able to read
# the following secret message:
#
#   Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
# Note that since English has 26 characters, your ROT-13 program will be able to both encode and decode texts written
# in English.
def caesar_cipher(phrase):
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
           'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
           'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
           'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
           'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
           'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
           'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
    result = ""
    for x in phrase:
        if x in key.keys():
            result += key[x]
        else:
            result += x
    return result


# Define a simple "spelling correction" function correct() that takes a string and sees to it that 1) two or more
# occurrences of the space character is compressed into one, and 2) inserts an extra space after a period if the
# period is directly followed by a letter. E.g. correct("This   is  very funny  and    cool.Indeed!") should return
# "This is very funny and cool. Indeed!" Tip: Use regular expressions!
def correct(phrase):
    multispace_regex = re.compile("\s{2,}").findall(phrase)
    nospace_regex = re.compile("(\w.*)([.])(\w.*)")
    for x in multispace_regex:
        phrase = phrase.replace(x, ' ')

    r = nospace_regex.split(phrase)
    phrase = ""
    for x in r:
        if x == ".":
            phrase += x + " "
        else:
            phrase += x
    return phrase

# The third person singular verb form in English is distinguished by the suffix -s,
# which is added to the stem of the infinitive form: run -> runs. A simple set of rules can be given as follows:
#
# If the verb ends in y, remove it and add ies
# If the verb ends in o, ch, s, sh, x or z, add es
# By default just add s
#
# Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form returns
# its third person singular form. Test your function with words like try, brush, run and fix. Note however that the
# rules must be regarded as heuristic, in the sense that you must not expect them to work for all cases.
# Tip: Check out the string method endswith().
def make_3sg_form(verb):
    other_ends = ["o", "ch", "s", "sh", "x", "z"]
    if str(verb).endswith("y"):
        verb = verb[0: -1] + "ies"
        return verb
    elif list((True for x in other_ends if verb.endswith(x))):
        verb = list((verb + "es" for x in other_ends if verb.endswith(x)))[0]
        return verb
    else:
        verb += "s"
        return verb


# In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going.
# A simple set of heuristic rules can be given as follows:
#
#If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
#If the verb ends in ie, change ie to y and add ing
#For words consisting of consonant-vowel-consonant, double the final letter before adding ing
#By default just add ing
#
#Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns
# its present participle form. Test your function with words such as lie, see, move and hug. However,
# you must not expect such simple rules to work for all cases.
def make_ing_form(verb):
    cvc_regex = re.compile("[^aeiou][aeiou][^aeiou]", re.IGNORECASE)
    if str(verb).endswith("ie"):
        verb = verb[0:-2] + 'ying'
    elif str(verb).endswith("e"):
        if str(verb).endswith("ee") or len(verb) < 3:
            verb += "ing"
        else:
            verb = verb[:-1] + "ing"
    elif cvc_regex.search(verb[-3:]):
        verb = verb + verb[-1] + "ing"
    else:
        verb += "ing"
    return verb