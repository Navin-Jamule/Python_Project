# List of characters used in the cipher (includes lowercase letters and digits 0-5)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            '0', '1', '2', '3', '4', '5']

# Taking user input for the operation type, message, and shift value
instruction = str(input('What do you want to perform - encode or decode: '))
original_text = str(input('What is the message you want to convert: '))
shift_amount = int(input('What is the amount of shift you want: '))

# Function to perform Caesar cipher encoding or decoding
def caesar_cipher(instruction, original_text, shift_amount):
    
    # Nested function to handle encoding (shifting letters forward)
    def encrypt(original_text, shift_amount):
        encode_text = ''
        for letter in original_text:
            # Find new shifted position by adding shift_amount
            shift_position = alphabet.index(letter) + shift_amount
            # Wrap around using modulo to stay within alphabet bounds
            shift_position %= len(alphabet)
            encode_text += alphabet[shift_position]
        print(f'Here is the encoded text: {encode_text}')

    # Nested function to handle decoding (shifting letters backward)
    def decrypt(encrypt_text, shift_amount):
        decode_text = ''
        for letter in encrypt_text:
            # Find original position by subtracting shift_amount
            shift_position = alphabet.index(letter) - shift_amount
            # Wrap around using modulo to stay within alphabet bounds
            shift_position %= len(alphabet)
            decode_text += alphabet[shift_position]
        print(f'Here is the decoded text: {decode_text}')
    
    # Based on user instruction, call the respective function
    if instruction == 'encode':
        encrypt(original_text, shift_amount)
    else:
        decrypt(original_text, shift_amount)

# Call the Caesar cipher function with user inputs
caesar_cipher(instruction, original_text, shift_amount)
