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

input2 = translate(message)

# Makes new decoded txt file
print(input2)
open('input2.txt', 'w').write(input2)
