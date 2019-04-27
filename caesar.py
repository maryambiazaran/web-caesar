import string
from helpers import alphabet_position, rotate_character

def rotate_string(text, rot):
    ''' This is the actual function that does the job! - more comment '''
    result = ''
    for c in text:
        result += rotate_character(c,rot)
    return result

def main():
    # your main code (input and print statements)
    from sys import argv
    user_input_message = input ('Type a message:')
    if len(argv)>1:
        user_input_rotation = int(argv[1])
    else:
        user_input_rotation = int(input ('Rotate by:'))
    print(rotate_string(user_input_message, user_input_rotation))

if __name__ == "__main__":
    main()