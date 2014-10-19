__author__ = 'cxa70'
import time
from pprint import pprint as pp

# region Very Simple Exercises
# from verysimpleexercises import *
# print(max(12, 24))
# print(maxofthree(3, 1, 7))
# print(length("my test string"))
# print(length([12, 234, 6345, 234213, 23452345, 234, 123]))
# print(length({(12, 45), (234,45), (1.234535, 2345)}))
# print(isvowel("a"))
# print(isvowel("apple"))
# print(isvowel(234))
# print(isvowel([1,23,4,56345]))
# print(translate("this is fun"))
# print(sum([1,2,3,4]))
# print(multiply([1,2,3,4]))
# print(reverse("I am testing"))
# print(is_palindrome("patsy"))
# print(is_palindrome("bob"))
# print(is_palindrome("radar"))
# print(is_member("x", "test value"))
# print(is_member("x", [12, 234, 3452346, "123", "x"]))
# print(overlapping([1,2,3,4,5,6],[7,8,9,10,11,12]))
# print(overlapping([1,2,3,4,5,6],[7,8,9,10,11,12,1]))
# print(generate_n_chars('x', 10))
# print(generate_n_chars('xz', 15))
# historgram([3, 2, 6])
# historgram([4,9,7])
# print(max_in_list([123,4,56,2,3,4,5,6,23,23456,2356,346,3467,7,7,48,48,6,2345,2345,2345,23,45,7,47,3456,48,58,7,234,5,2347]))
# print(map_lengths(["test","one","fallow"]))
# print(find_longest_word(["apple","bottom","jeans","supercalifragilistic"]))
# print(filter_long_words(['foo', 'bang','crash'], 3))
# print(is_palindrome_phrase("Was it a rat I saw?"))
# print(is_palindrome_phrase("Tango Charlie"))
# print(is_pangram("The quick brown fox jumps over the lazy dog"))
# print(is_pangram("The buick brown fox jumps over the lazy dog"))
# print(get_99btls_lyrics(99))
# print(translate_swede("Merry Christmas"))
# pprint.pprint(char_freq("The buick brown fox jumps over the lazy dog"))
# print(caesar_cipher("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"))
# print(correct("This   is  very funny  and    cool.Indeed!"))
# print(make_3sg_form("run"))
# print(make_3sg_form("carry"))
# print(make_3sg_form("coach"))
# print(make_ing_form("run"))
# print(make_ing_form("carry"))
# print(make_ing_form("be"))
# print(make_ing_form("see"))
# print(make_ing_form("travel"))
# print(make_ing_form("boogie"))
# endregion

#region Higher Order Functions and list comprehensions
# from highorderfunctions import *
#
# pp(max_in_list([1, 2342, 3, 4, 5, 6]))
# pp(map_words(['test', 'other', 'words']))
# pp(find_longest_word(["this", "this is a test", "TheOther"]))
# pp(filter_long_words(["test1", "test of another word", "the"], 5))
# pp(translate(["merry", 'christmas', 'and', 'happy', 'new', 'year']))
#endregion

#region Simple IO exercises
from simpleIO import *

# print_palindromes('testfile.txt')
# pp(find_semordnilaps('testwordlist.txt'))
# pp("Characters sorted by frequency:")
# pp(char_freq_table('testfile.txt', 1))
# pp("Characters sorted by character:")
# pp(char_freq_table('testfile.txt', 0))
# speak_ICAO("this is a test", 0, 1)
# pp(get_hapaxes("testfile.txt"))
# pp(number_lines("testfile.txt", "newfile.txt"))
# pp(get_avg_word_len("testwordlist.txt"))
# guess_number_game()
# guess_word_game()
# lingo()
#endregion

#region Harder Exercises
from harder import *


# text_splitter("splitText.txt", "Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't.")
# find_anagrams("unixdict.txt")
# bracket_string_analyser(bracket_string_generator(10)))
# words_domino()
find_alternades()
#endregion