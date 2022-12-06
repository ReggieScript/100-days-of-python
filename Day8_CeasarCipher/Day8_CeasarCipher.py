alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)

cont='yes'


def encrypt(txt,shft):
  encoded_text=""
  for i in txt:
    if i ==" ":
      encoded_text=encoded_text+ " "
    else:
      for n in alphabet:
        if n==i:
          encoded_text=encoded_text+alphabet[(alphabet.index(n)+shift)]
  return encoded_text

def decrypt(txt,sgft):
  decoded_text=""
  for i in txt:
    if i == " ":
      decoded_text=decoded_text+" "
    else:
      for n in alphabet:
        if n==i:
          decoded_text=decoded_text+alphabet[(alphabet.index(n)-shift)]
  return decoded_text

while cont == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == 'encode':
    print('Your encrypted message is: ',encrypt(text,shift))
  elif direction =='decode':
    print('Your decoded message is: ',decrypt(text,shift))
  cont=input("Would you like to continue? Type 'yes'or 'no'\n")

print("Thank's for using our ceasar cipher :D")   