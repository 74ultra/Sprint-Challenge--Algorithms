'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) < len('th'):
        return 0
    if word[:2] == 'th':
        return 1 + count_th(word[1:])
    return count_th(word[1:])


"""
Accepts single word as parameter
if the word length is shorter that the the length of the target letter combo, return 0
if the letters at the first two index positions equal 'th', return 1 + the value of the function passed with the word minus its first index
if the letters do not equal 'th', return the value of the function passed with the word minus its first index
"""
