alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

continueChoice = "yes"

def encrypt(data,shiftNum):
  listStr = list(data)
  for x in range(len(listStr)):
    index = alphabet.index(listStr[x])
    if(index + shiftNum < 26):
      listStr[x] = alphabet[index + shiftNum]
    else:
      listStr[x] = alphabet[index + shiftNum - 26]
        

  print(encodedStr.join(listStr))

def decrypt(data,shiftNum):
  listStr = list(data)
  for x in range(len(listStr)):
    index = alphabet.index(listStr[x])
    if(index - shiftNum < 0):
      listStr[x] = alphabet[index - shiftNum + 26]
    else:
      listStr[x] = alphabet[index - shiftNum]
  print(decodedStr.join(listStr))

print(logo)
while (continueChoice == "yes"):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  encodedStr = ""
  decodedStr = ""

  if( direction == "encode"):
    encrypt(text,shift)
  elif( direction == "decode"):
    decrypt(text,shift)
  else:
    print("Please choose the correct option") 

  continueChoice = input("Do you want to check again ? Yes or No : ").lower()     
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  encode

    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
