alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  text_list = list(text)
  text_shifted = ''
  
  for i in range(len(text_list)):
    #loop each alphabet + shift --> return shift alphabet from alphabet[default + shift]
    text_shifted += alphabet[alphabet.index(text_list[i]) + shift]
  #print ciphet text that already shifted
  print(f"The encoded text is {text_shifted}")
#triggered function
encrypt(text, shift)

