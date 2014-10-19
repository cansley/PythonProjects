import re
from pprint import pprint as pp
import random

# A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for
# sentence splitting includes (but isn't limited to) the following rules:
#
# Sentence boundaries occur at one of "." (periods), "?" or "!", except that
#
# Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
# Periods followed by a digit with no intervening whitespace are not sentence boundaries.
# Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are not
# sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.
# Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for example,
# www.aptex.com, or e.g).
# Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries
# .
# Your task here is to write a program that given the name of a text file is able to write its content with each
# sentence on a separate line. Test your program with the following short text:
# Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks
# he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't.
#
# The result should be:
#
# Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
# Did he mind?
# Adam Jones Jr. thinks he didn't.
# In any case, this isn't true...
# Well, with a probability of .9 it isn't.
def text_splitter(file_path, file_content):
    file_content = str(file_content)
    digits = range(0, 9)
    titles = ["Mr.", "Ms.", "Mrs.", "Jr.", "Dr."]
    consenants = re.compile("[a-z]", re.IGNORECASE)
    line_break_idx = []
    segments = []
    idx = 0
    while idx != -1:
        idx = file_content.find("?", idx + 1)
        if idx != -1:
            line_break_idx.append(idx)

    idx = 0
    while idx != -1:
        idx = file_content.find("!", idx + 1)
        if idx != -1:
            line_break_idx.append(idx)

    idx = 0
    while idx != -1:
        idx = file_content.find(".", idx + 1)
        if idx != -1:
            if idx == len(file_content) - 1:
                idx = -1
                continue
            if file_content[idx - 2: idx + 1] in titles or file_content[idx - 3:idx + 1] in titles:
                continue
            if (file_content[idx - 1] in digits or file_content[idx - 1] == " ") and file_content[idx + 1] in digits:
                continue
            if consenants.match(file_content[idx - 1]) and file_content[idx - 2] == ".":
                continue
            if file_content[idx + 1] == " " and consenants.match(file_content[idx + 2]):
                line_break_idx.append(idx)
    last_idx = 0
    for x in sorted(line_break_idx):
        segments.append((last_idx, x + 2))
        last_idx = x + 2

    with open(file_path, "w+") as f:
        for x in segments:
            f.write(file_content[x[0]: x[1]] + "\n")
        f.write(file_content[last_idx:])


# An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or
# phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at
# http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that share the same
# characters that contain the most words in them.
class dictionary_word(object):
    def __init__(self):
        self.Value = ""
        self.Length = 0
        self.CharList = []

    def populate(self, source: str):
        self.Value = source
        self.Length = len(source)
        self.CharList = sorted(source)
        return self

    def isAnagram(self, comparator):
        return self.Length == comparator.Length and self.Value != comparator.Value and self.CharList == comparator.CharList


def find_anagrams(word_list_file):
    master_word_list = []
    with open(word_list_file) as f:
        for line in f:
            newWord = dictionary_word().populate(line.replace("\n", "").lower())
            master_word_list.append(newWord)
            # master_word_list = list(map(lambda x: dictionary_word().populate(x.replace("\n", "").lower()), f))

    master_anagram_list = []
    while len(master_word_list) > 0:
        word = master_word_list.pop()
        anagram_list = [word.Value]
        filter_list = list(
            filter(lambda n: word.Length == n.Length and word.Value != n.Value and word.CharList == n.CharList,
                   master_word_list))
        anagram_list.extend(map(lambda z: z.Value, filter_list))
        for zed in filter_list:
            if zed in master_word_list:
                master_word_list.remove(zed)
        master_anagram_list.append(anagram_list)
    master_anagram_list = sorted(master_anagram_list, key=len)
    max_len = len(master_anagram_list[-1])
    pp(list(filter(lambda x: len(x) == max_len, master_anagram_list)))


# Your task in this exercise is as follows:
#
# Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
# Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing
# brackets (in that order), none of which mis-nest.
# Examples:
#
# []        OK   ][        NOT OK
#    [][]      OK   ][][      NOT OK
#    [[][]]    OK   []][[]    NOT OK
def bracket_string_generator(bracket_count):
    ret_string = ""
    bracket_array = ["[", "]"]
    for i in range(0, bracket_count):
        rnd_num = random.randint(1, 10000) % 2
        ret_string += bracket_array[rnd_num]
    return ret_string


def bracket_string_analyser(string_to_eval):
    pp("Analysing string: " + string_to_eval)
    is_balanced = True
    bal_count = 0
    for c in string_to_eval:
        if c == "[":
            bal_count += 1
        if c == "]":
            bal_count -= 1
        if bal_count < 0:
            is_balanced = False
            break
    is_balanced = bal_count == 0
    pp("String is balanced? " + str(is_balanced))


#A certain childrens game involves starting with a word in a particular category. Each participant in turn says a word,
# but that word must begin with the final letter of the previous word. Once a word has been given, it cannot be repeated
# . If an opponent cannot give a word in the category, they fall out of the game. For example, with "animals" as the
# category,
#
# Child 1: dog
# Child 2: goldfish
# Child 1: hippopotamus
# Child 2: snake
# ...
# Your task in this exercise is as follows: Take the following selection of 70 English Pokemon names (extracted from
# Wikipedia's list of Pokemon) and generate the/a sequence with the highest possible number of Pokemon names where the
# subsequent name starts with the final letter of the preceding name. No Pokemon name is to be repeated.
#
# audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
# cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
# girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
# kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
# nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
# porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
# sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
# tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask
def build_list(string_to_parse):
    return list(str(string_to_parse).split())


def add_to_dict(value_to_add, dict):
    dict.setdefault(value_to_add, 0)
    dict[value_to_add] += 1


def word_starts_with(letter, word_list):
    return list(filter(lambda x: x[0] == letter, word_list))


def word_ends_with(letter, word_list):
    return list(filter(lambda x: x[-1] == letter, word_list))


def sort_list_by_freq(freq_list, target_list):
    cross_sorted_list = []
    for l in freq_list:
        x = word_ends_with(l, target_list)
        cross_sorted_list.extend(x)
        for z in x:
            target_list.remove(z)
    for z in target_list:
        cross_sorted_list.append(z)
    return cross_sorted_list


def build_sub_list(current_word, master_list):
    max_list, series = [], []
    series.append(current_word)
    work_list = master_list[:]
    if current_word in work_list:
        work_list.remove(current_word)
    inner_list = word_starts_with(current_word[-1], work_list)
    for w in inner_list:
        series.extend(build_sub_list(w, work_list))
        if len(series) > len(max_list):
            max_list = series[:]
        series = [current_word]
    if len(series) > len(max_list):  # this needs to be here to catch items with no inner_list results
        max_list = series[:]
    return max_list


def words_domino():
    word_list = build_list(
        "audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk"
        " darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran"
        " ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone"
        " machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena"
        " porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty "
        " sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue"
        " vigoroth vulpix wailord wartortle whismur wingull yamask")

    max_list, series = [], []
    for word in word_list:
        current_word = word
        work_list = word_list[:]
        work_list.remove(current_word)
        series = build_sub_list(current_word, work_list)
        if len(series) > len(max_list):
            max_list = series[:]

    pp(max_list)


#An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as
# the original word, make up at least two other words. All letters must be used, but the smaller words are not
# necessarily of the same length. For example, a word with seven letters where every second letter is used will produce
# a four-letter word and a three-letter word. Here are two examples:
#
#   "board": makes "bad" and "or".
#   "waists": makes "wit" and "ass".
# Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that goes through each word
#  in the list and tries to make two smaller words using every second letter. The smaller words must also be members of
# the list. Print the words to the screen in the above fashion.
def get_even_odd_words(word, starting_pos, lookup_list):
    output = ""
    for x in range(starting_pos, len(word), 2):
        output += word[x]

    if len(output) >= 2 and output in lookup_list:
        return output
    else:
        return ""


def find_alternades():
    with open('unixdict.txt', mode='r') as file:
        word_list = []
        for line in file:
            word_list.append(line.replace('\n', ''))

    for word in word_list:
        odd_letters = get_even_odd_words(word, 1, word_list)
        even_letters = get_even_odd_words(word, 0, word_list)

        if len(even_letters) > 0 or len(odd_letters) > 0:
            if len(even_letters) == 0:
                message = '"%s": makes "%s".' % (word, odd_letters)
            elif len(odd_letters) == 0:
                message = '"%s": makes "%s".' % (word, even_letters)
            else:
                message = '"%s": makes "%s" and "%s".' % (word, even_letters, odd_letters)
            pp(message)
