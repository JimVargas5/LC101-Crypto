#Jim Vargas helpers
import string

def alphabet_position(letter):
    '''Returns a pseudo ord position of a letter'''
    #This part starts up a Reference List for the letters: [[a,A],[b,B],...]
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    RefList = [[0 for i in range(2)] for j in range(26)]
    for group in range(len(RefList)):
        RefList[group][0] = lowers[group]
        RefList[group][1] = uppers[group]

    #This checks to see if letter is a letter
    temp = uppers+lowers
    if temp.count(letter) < 1:
        return letter

    #This part is the mechanism that fulfills the function's purpose
    for group in range(len(RefList)):
        if RefList[group][0] == letter:
            return group
        if RefList[group][1] == letter:
            return group


def rotate_character(char, rot):
    '''Returns a new letter based on a given letter and "rotation" factor
        across a pseudo ord circle'''
    #This part starts up a Reference List for the letters: [[a,A],[b,B],...]
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    RefList = [[0 for i in range(2)] for j in range(26)]
    for group in range(len(RefList)):
        RefList[group][0] = lowers[group]
        RefList[group][1] = uppers[group]

    #This checks to see if char is a letter
    temp = uppers+lowers
    if temp.count(char) < 1:
        return char

    #This part is the mechanism that fulfills the function's purpose
    position = alphabet_position(char)
    Intended = (position + rot) % 26
    CapOrNaw = 2
    for letter in range(len(lowers)):
        if char == lowers[letter]:
            CapOrNaw = 0
        if char == uppers[letter]:
            CapOrNaw = 1
    return RefList[Intended][CapOrNaw]