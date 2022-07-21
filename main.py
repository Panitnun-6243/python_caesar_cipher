import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#fix shift bug (number of shift greater than the number of letters in the alphabet)
if shift > 26:
  shift = shift%26
#create caesar function to combine all function
def caesar(text, shift, direction):
  #encrypt
  def encrypt(text, shift):
    text_list = list(text)
    text_shifted = ''
  
    for i in range(len(text_list)):
      #loop each alphabet + shift --> return shift alphabet from  alphabet[default + shift]
      text_shifted += alphabet[alphabet.index(text_list[i]) + shift]
    #print cipher text that already shifted
    print(f"The encoded text is {text_shifted}")

  #decrypt
  def decrypt(text, shift):
    text_list = list(text)
    text_decrypted = ''

    for letter in text_list:
      #the same logic as encrypted but different way to code
      old_position = alphabet.index(letter)
      text_decrypted += alphabet[old_position - shift]
    #print decrypt text that already unshifted
    print(f"The decoded text is {text_decrypted}")

  #Check what user wanted
  if direction == "encode":
    encrypt(text, shift)
  elif direction == "decode":
    decrypt(text, shift)

#trigger function
caesar(text, shift, direction)



