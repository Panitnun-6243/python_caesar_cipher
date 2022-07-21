import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
play_again = True
while play_again == True:
  print()
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
        if text_list[i] in alphabet:
          text_shifted += alphabet[alphabet.index(text_list[i]) + shift]
        else:
          text_shifted += text_list[i]
      #print cipher text that already shifted
      print(f"Here's the encoded result: {text_shifted}")
        
  
    #decrypt
    def decrypt(text, shift):
      text_list = list(text)
      text_decrypted = ''
  
      for letter in text_list:
        #the same logic as encrypted but different way to code
        if letter in alphabet:
          old_position = alphabet.index(letter)
          text_decrypted += alphabet[old_position - shift]
        else:
          text_decrypted += letter
      #print decrypt text that already unshifted
      print(f"Here's the decoded result: {text_decrypted}")
  
    #Check what user wanted
    if direction == "encode":
      encrypt(text, shift)
    elif direction == "decode":
      decrypt(text, shift)
  
  #trigger function
  caesar(text, shift, direction)
  
  #ask user for restarting the program?
  print()
  ans = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

  if ans == "yes" or ans == "y":
    play_again = True
  elif ans == "no" or ans == "n":
    play_again = False

