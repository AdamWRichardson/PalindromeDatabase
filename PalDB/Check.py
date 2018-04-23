#! /usr/bin/env python2.7
__author__ = "Adam Richardson"
__Date__ = 18 / 04 / 18

# Don't need any imports just make it general.

# Remove all punctuation from users string
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''' '


def check(list_of_palindromes):
    # Need a way of taking the user input, from there check if i   t's a palindrome
    # String input in request forms is the name of the box in the html file home.html
    word = list_of_palindromes
    no_punc = ''
    for char in word:
        if char not in punc:
            no_punc = (no_punc + char).lower()
    cond = no_punc == no_punc[::-1]
    return cond
