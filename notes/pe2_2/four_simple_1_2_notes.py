# Caesar cipher.

# Ask the user to enter a message.
text = input("Enter your message: ")

# Initialize an empty string to store the encrypted message.
cipher = ''

# Iterate over each character in the input message.
for char in text:
    # Check if the character is not alphabetic.
    if not char.isalpha():
        # If it's not alphabetic, skip to the next character.
        continue
    
    # Convert the character to uppercase for consistency.
    char = char.upper()
    
    # Shift the character by one position in the alphabet.
    code = ord(char) + 1
    
    # If the shifted character exceeds 'Z', wrap around to 'A'.
    if code > ord('Z'):
        code = ord('A')
    
    # Append the encrypted character to the cipher string.
    cipher += chr(code)

# Print the encrypted message.
print(cipher)


# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)