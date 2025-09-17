def create_coding():
    print("Enter a 26-character string for the code (a-z):")
    code_str = input().strip().lower()
    return code_str


def is_code_correct(code):
    if len(code) != 26:
        return False

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if code.count(char) != 1:
            return False

    return True

def encode_string(code, text):
    original_alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_text = ""
    for char in text.lower():
        if 'a' <= char <= 'z':
            index = original_alphabet.find(char)
            encoded_char = code[index]
            encoded_text += encoded_char
        else:
            encoded_text += char  # Keep non-alphabet characters as they are
    return encoded_text


coding = create_coding()

if is_code_correct(coding):
    print("Code is correct. Enter lines to encode (press Enter on an empty line to finish):")

    while True:
        line_to_encode = input()
        if not line_to_encode:
            break

        encoded_line = encode_string(coding, line_to_encode)
        print(encoded_line)
else:
    print("Invalid code. Please ensure it contains all 26 unique letters.")