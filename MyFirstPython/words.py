"""Module Level Documentation

Usage:
    How to use this...

"""
__author__ = 'cxa70'

from urllib.request import urlopen

def fetch_words():
    '''Retrieves a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from the document.
    '''
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    for word in story_words:
        print(word)  # This is a line comment...use these sparingly...
