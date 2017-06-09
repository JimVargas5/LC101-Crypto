#Jim Vargas caesar
import string
from helpers import rotate_character, alphabet_position
from sys import argv, exit

def encrypt(text, rot):
    '''Encrypts a text based on a pseudo ord circle caesar style'''
    NewString = ""
    for character in text:
        NewChar = rotate_character(character, rot)
        NewString = NewString + NewChar
    return NewString


def main(rot):
    if rot.isdigit():
        text = input("Type the message that you would like to encrypt: ")
        #rot = int(input(Rotate by:))
        rot = int(rot)
        print(encrypt(text, rot))
    else:
        print("You need to enter an integer argument.")
        exit()


if __name__ == '__main__':
    if len(argv) <=1:
        print("You need to enter an integer argument.")
        exit()
    else:
        main(argv[1])