#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def login():
    print("******Login Page*******")
    print("1. NEW USER ")
    print("2. EXISTING USER ")
    ch=int(input("ENTER YOUR CHOICE-->>"))
    if ch==1:
        name=input("ENTER YOUR NAME----->")
        pwd=input("ENTER A PASSWORD----->")
        lower=0
        upper=0
        special=0
        digit=0
        if(len(pwd)>=8):
            for i in pwd:
                if (i.islower()):
                    lower+=1
                if (i.isupper()):
                    upper+=1
                if (i=='_' or i=='$' or i=='@'):
                    special+=1
                if (i.isdigit()):
                    digit+=1
        if (lower>=1 and upper>=1 and special>=1 and digit>=1):
            print("!ACCOUNT CREATED!")
        else:
            print("!INVALID PASSWORD!")
            print("!Password must be atleast 6 characters long!")
            print("!Password must contain atleast one digit,atleast one lower case and atleast one upper case,atleast one special character ")
        f=open('users.txt','a')
        f.write(name)
        f.write(pwd)
        f.close()
    elif ch==2:
        n=input("ENTER YOUR NAME----->")
        pas=input("ENTER A PASSWORD----->")
        file = open("users.txt")
        if(n in file.read() and pas in file.read()):
            print("!LOGGED IN!")
        else:
            print("!INVALID!")
    else:
         print("!INVALID!")

