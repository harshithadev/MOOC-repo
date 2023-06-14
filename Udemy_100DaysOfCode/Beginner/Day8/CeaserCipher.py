from base64 import encode
import string
# def returnindex():
#     if ((alphabets.index(letter)-key)>-1):
#         return (alphabets.index(letter)-key)%26
#     else: 
#         return (26-)
alphabets = string.ascii_lowercase
option = int(input("Encode or Decode : 1, 2 -> "))
text = input("Enter the text : ")
key = int(input("Cipher key : "))
newtext = ""
if(option == 1):
    for letter in text:
        newtext += alphabets[(alphabets.index(letter)+key)%26]
    print(f"Encoded text is : {newtext}")
else: 
    for letter in text:
        newtext += alphabets[(alphabets.index(letter)-key)%26]
    print(f"Encoded text is : {newtext}")
    
    
#can modify it using functions, and then furthur modify it by merging two fuctions into one function!
