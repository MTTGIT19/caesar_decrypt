# Reversing rot13 encyption
def translate(msg):
    translated = ""
    for symbol in msg:
      if symbol in LETTERS:
        num = LETTERS.find(symbol)
        num = (num - key) % 26
        translated = translated + LETTERS[num]
    return translated


message = open('location_of_file', 'r').read()

key = 13

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = message.upper()

output = translate(message)

# Prints output to new txt file
print(output)
open('Decrypted_file.txt', 'w').write(output)
