import string
def alphabet_position(letter):
    """ This function gives the position of the given letter """
    if letter in string.ascii_lowercase:
        return ord(letter) - ord('a')
    elif letter in string.ascii_uppercase:
        return ord(letter) - ord('A')

def rotate_character(char, rot):
    if char in string.ascii_lowercase:
        return string.ascii_lowercase[(alphabet_position(char)+rot) % 26]
    elif char in string.ascii_uppercase:
        return string.ascii_uppercase[(alphabet_position(char)+rot) % 26]
    else:
        return char