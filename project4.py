print("caesal_ciphal")
n = int(input("enter number of shift:"))
message = input("type message:")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
def caesal_ciphe(messagee,nn):
    n=int(input("enter number of shift:"))
    message=input("type message:")
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #encrypted message
    newmessage=""
    for char in message:
        position=alphabet.index(char)
        new_position=(position+n)%26

        newmessage=newmessage+alphabet[new_position]
    print(f"plain_text is:{newmessage}")


caesal_ciphe(messagee="message",nn="n")
decryptmessage=""
def decrypt(newmessage,nn):
    for char in newmessage:
        positio=alphabet.index(char)
        new_positi=(positio-n)%26
    -decryptmessage=decryptmessage+alphabet(new_positi)
    print(f"decrupt message is :{decryptmessage}")
decrypt(message,n)
