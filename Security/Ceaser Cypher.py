#Ceaser Cypher
#Carlo Gonzalez Networking

ref = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!? "
refLen = (len(ref) + 1)

text = ""

while (text == ""):
    text = input ("What is your message?: ")
    if text == "":
        print ("Please input a message: ")
        
cryption =  input("encrypt or decrypt:  ")

print(text + " " + cryption)
 
key = int(ref.find(len(text) % refLen))
print(key)

          
if cryption == encrypt:
    message = ""
    while text != "":
        #shift by key
        shift = int((ref.find(text.pop()) + key) % refLen)
        message = ref[shift] + message 

        
    print(message)
    
elif cryption == decrypt :


    print (text)
    
else:
    print ("please choose encrypt or decrypt")