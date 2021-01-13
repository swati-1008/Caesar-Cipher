alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  result = ''
  for letter in text:
    if letter not in alphabet:
      result += letter
    else:
      ind = alphabet.index(letter)
      if direction == 'encode':
        ind = (ind + shift) % 26
      elif direction == 'decode':
        ind = (ind - shift) % 26
      result += alphabet[ind]

  print('The ' + direction + 'd text is ' + result)

from art import logo
print(logo)

while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift, direction)
  loop = input("Do you wish to continue? Type yes or no. ")
  if loop == 'no':
    print('Goodbye')
    break
