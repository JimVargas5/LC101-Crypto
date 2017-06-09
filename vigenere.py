#Jim Vargas vigenere
import string
from helpers import rotate_character, alphabet_position
from sys import argv, exit

def encrypt(text, key):
    '''Encrypts a text based on a pseudo ord circle vigenere style'''
    #This part creates a reference list for how much to rotate each character
    #in text, based on the key
    RotList = []
    ShiftCount = 0
    for idx in range(len(text)):
        test = text[idx].isalpha()
        RotList = RotList + [" "]
        KeyMod = idx % len(key)
        if test == False:
            RotList.insert(idx, " ")
            ShiftCount = ShiftCount + 1
        RotList[idx + ShiftCount] = key[KeyMod]
        #print(idx, RotList)

    #This part is the mechanism that fulfills the function's purpose
    NewString = ""
    for idx in range(len(text)):
        NewChar = rotate_character(text[idx], alphabet_position(RotList[idx]))
        NewString = NewString + NewChar
    return NewString


def main(key):
    if key.isalpha():
        text = input("Type the message that you would like to encrypt: ")
        #key = input("Encryption key:")
        print(encrypt(text, key))
    else:
        print("You need to enter a key with only alphabetic letters;", 
        "no symbols, numbers, spaces or other characters.")
        exit()


if __name__ == '__main__':
    if len(argv) == 2:
        main(argv[1])
    else:
        print("You need to enter a key with only alphabetic letters;", 
        "no symbols, numbers, spaces or other characters.")
        exit()