# text = 'Hello World' # (variable declaration) variable_name = (assignment operand) value
# print(text) # use print() function (reusable code block that can call (run) when needed)
# print(text[6]) # access character at index 6
# print(text[-1]) # access the last character
# print(len(text)) # use len() function to access the nr of characters
# print(type(text)) # type() to return the data type of variable
# python uses snake_case, and is case sensitive. Snake_Case, snake_Case, SNAKE_case, snake_CASE = all different
# method = a function that belongs to an object

"""Caesar cipher"""
# take each letter in your message, find its position in the alphabet
# take the letter located after 3 positions, and replace the original letter with the new letter
text = 'Hello World!'
shift = 3


def caesar(message, offset):
    alphabet = 'abcdefghijklomnoqrstuvwxyz'
    encrypted_text = ''
    for char in message.lower():
        # append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    print('plain text:', message)
    print('encrypted text:', encrypted_text)


caesar(text, shift)
caesar(text, 13)

