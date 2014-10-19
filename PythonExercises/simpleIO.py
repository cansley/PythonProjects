from pprint import pprint as pp
import re
import os
import time
import win32com.client
import functools
import random
import getpass

# Write a version of a palindrome recogniser that accepts a file name from the user, reads each line,
# and prints the line to the screen if it is a palindrome.
def print_palindromes(filePath):
    file = open(filePath)
    char_regex = re.compile("[a-z]", re.IGNORECASE)
    for line in file:
        stripped = ''.join(char_regex.findall(line)).lower()
        if stripped == ''.join(reversed(stripped)):
            pp(line)


# According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards.
# ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name
# (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps to the
# screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair
# "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!
def find_semordnilaps(filePath):
    file = open(filePath)
    wordlist = []
    finallist = []
    for line in file:
        for word in line.split():
            wordlist.append(word)

    for x in wordlist:
        for y in wordlist:
            if x.lower() == ''.join(reversed(y)).lower():
                combined = x + ' ' + y
                inverted = y + ' ' + x
                if combined not in finallist and inverted not in finallist:
                    finallist.append(combined)
    return finallist


# Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user,
# builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted
# character frequency table to the screen.
def char_freq_table(file_path, sort_index):
    f = open(file_path)
    char_dict = {}
    for line in f:
        for c in line:
            if c not in char_dict.keys():
                char_dict[c] = 1
            else:
                char_dict[c] += 1

    finallist = []
    for x in char_dict.keys():
        finallist.append((x, char_dict[x]))

    return sorted(finallist, key=lambda x: x[sort_index])


# The International Civil Aviation Organization (ICAO) alphabet assigns code words to the letters of the English
# alphabet acrophonically (Alfa for A, Bravo for B, etc.) so that critical combinations of letters (and numbers)
# can be pronounced and understood by those who transmit and receive voice messages by radio or telephone regardless
# of their native language, especially when the safety of navigation or persons is essential. Here is a Python
# dictionary covering one version of the ICAO alphabet:
#
# d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
# 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
# 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
#      's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
#      'x':'x-ray', 'y':'yankee', 'z':'zulu'}
#
# Your task in this exercise is to write a procedure speak_ICAO() able to translate any text (i.e. any string) into
# spoken ICAO words. You need to import at least two libraries: os and time. On a mac, you have access to the system
# TTS (Text-To-Speech) as follows: os.system('say ' + msg), where msg is the string to be spoken. (Under UNIX/Linux
# and Windows, something similar might exist.) Apart from the text to be spoken, your procedure also needs to accept
# two additional parameters: a float indicating the length of the pause between each spoken ICAO word, and a float
# indicating the length of the pause between each word spoken.
def speak_ICAO(text_to_speak, char_pause, word_pause):
    word_list = text_to_speak.split()
    d = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot',
         'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
         'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec', 'r': 'romeo',
         's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey',
         'x': 'x-ray', 'y': 'yankee', 'z': 'zulu'}

    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    for word in word_list:
        for char in word:
            if char in d.keys():
                speaker.Speak(d[char])
                #os.system('say ' + d[char])
                time.sleep(char_pause)
        time.sleep(word_pause)


# A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a
# language, the works of an author, or in a single text. Define a function that given the file name of a text will
# return all its hapaxes. Make sure your program ignores capitalization.
def get_hapaxes(file_path):
    f = open(file_path)
    word_list = {}
    for line in f:
        for word in line.split():
            if word.lower() not in word_list.keys():
                word_list[word.lower()] = 1
            else:
                word_list[word.lower()] += 1
    final_list = []
    for x in word_list.keys():
        if word_list[x] == 1:
            final_list.append(x)
    return final_list


# Write a program that given a text file will create a new text file in which all the lines from the original
# file are numbered from 1 to n (where n is the number of lines in the file).
def number_lines(source_file, dest_file):
    ct = 0
    with open(source_file) as s:
        with open(dest_file, 'w+') as d:
            for line in s:
                d.write(str(ct) + '. ' + line)
                ct += 1
    return "Wrote %s lines." % str(ct)


# Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the
# lengths of the word tokens in the text, divided by the number of word tokens).
def get_avg_word_len(file_path):
    lengths = []
    with open(file_path) as f:
        for line in f:
            for word in line.split():
                lengths.append(len(word))
    return functools.reduce(lambda x, y: x + y, lengths) / len(lengths)


# Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen
# between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a terminal:
#
# >>> import guess_number
# Hello! What is your name?
# Torbjörn
# Well, Torbjörn, I am thinking of a number between 1 and 20.
# Take a guess.
# 10
# Your guess is too low.
# Take a guess.
# 15
# Your guess is too low.
# Take a guess.
# 18
# Good job, Torbjörn! You guessed my number in 3 guesses!
def guess_number_game():
    user_name = input("Hello! What is your name?\n")
    num_to_guess = random.randrange(1, 20)
    guess_count = 0
    guess_value = 0
    pp("Well %s, I am thinking of a number between 1 and 20." % user_name)
    while guess_value != num_to_guess:
        guess_count += 1
        guess_value = int(input("Take a guess.\n"))
        if guess_value == num_to_guess:
            pp("Good job, %s! You guessed my number in %d guesses!" % (user_name, guess_count))
            return
        elif guess_value < num_to_guess:
            pp("Your guess is too low.")
        elif guess_value > num_to_guess:
            pp("Your guess is too high.")


# An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new
# word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse, A decimal point =
# I'm a dot in place. Write a Python program that, when started
#      1) randomly picks a word w from given list of words,
#      2) randomly permutes w (thus creating an anagram of w),
#      3) presents the anagram to the user, and
#      4) enters an interactive loop in which the user is invited to guess the original word.
# It may be a good idea to work with (say) colour words only. The interaction with the program may look like so:
#
# >>> import anagram
# Colour word anagram: onwbr
# Guess the colour word!
# black
# Guess the colour word!
# brown
# Correct!
def guess_word_game():
    word_list = ['red', 'green', 'brown', 'black', 'purple']
    target_word = word_list[random.randrange(0, len(word_list))]
    anagram = ''
    idxlist = []
    while len(idxlist) < len(target_word):
        rnd = random.randrange(0, len(target_word))
        if rnd not in idxlist:
            idxlist.append(rnd)
    for x in idxlist:
        anagram += target_word[x]
    pp("Color word anagram: %s" % anagram)
    guess_word = ""
    while guess_word != target_word:
        guess_word = input("Guess the colour word!\n")
    pp("Correct!")


# In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this word by
# guessing, and in return receive two kinds of clues: 1) the characters that are fully correct, with respect to
# identity as well as to position, and 2) the characters that are indeed present in the word, but which are placed
# in the wrong position. Write a program with which one can play Lingo. Use square brackets to mark characters correct
# in the sense of 1), and ordinary parentheses to mark characters correct in the sense of 2). Assuming, for example,
# that the program conceals the word "tiger", you should be able to interact with it in the following way:
#
# >>> import lingo
# snake
# Clue: snak(e)
# fiest
# Clue: f[i](e)s(t)
# times
# Clue: [t][i]m[e]s
# tiger
# Clue: [t][i][g][e][r]
def lingo():
    input_word = getpass.getpass(prompt="Enter word to guess:\n")
    guess_word = ""
    while input_word != guess_word:
        response = ""
        guess_word = input("Enter your guess:\n")
        if input_word == guess_word:
            pp("Good job! The word was indeed %s" % input_word)
            return
        for x in range(0, len(guess_word)):
            char = guess_word[x]
            if x < len(input_word) and input_word[x] == char:
                char = "[" + char + "]"
            elif x < len(input_word) and char in input_word:
                char = "(" + char + ")"
            response += char
        pp("Clue: %s" % response)