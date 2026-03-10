from skpy import Skype
import os.path


slogin = Skype("aakankshabalode@gmail.com","password")


contact = slogin.contacts["live: .cid.2405"]
with open("C:\Users\Downloads\skp.png", "rb") as f:
          contact.chat.sendFile(f, "skp.png", image= True)


group = slogin.chats.create(["live: "])

contact = slogin.contacts["live: .cid.2405"]
contact.chat.sendMsg("welcome to bioinformatics world")

for i in contact:
    print(i)
    
