#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
def genKeys():
    pierwsze = genPierwsze();
    pierwsza1, pierwsza2 = 0, 0
    pub = 0
    priv = 0
    arrLen = len(pierwsze)
    while pierwsza1 == pierwsza2:
        pierwsza1=losujPierwsza(pierwsze, arrLen)
        pierwsza2=losujPierwsza(pierwsze, arrLen)
    phi = euler(pierwsza1, pierwsza2)
    n = modul(pierwsza1, pierwsza2)
    e = 2
    e_w=[]
    while e<phi:
        if NWD(e, phi)==1:
            e_w.append(e)
        e+=1
    e1=random.randint(0, len(e_w)-1)
    e=e_w[e1]
    d=mod1(e, phi)
    return str("Klucz publiczny [{},{}]; Klucz prywatny [{},{}]".format(e,n,d,n))


# In[ ]:





# In[14]:


def genPierwsze():
    ile=500
    pierwsze=[]
    num = 0
    x=2
    while num < ile:
        prop=True
        y=2
        while y*y<=x:
            if x%y==0:
                prop=False
                break
            y+=1
        if prop==True:
            pierwsze.append(x)
            num+=1
            x+=1
        else:
            x+=1
    return pierwsze


# In[3]:


def losujPierwsza(arr, length):
    return int(arr[random.randint(0,length-1)])


# In[4]:


def euler(a,b):
    return (a-1)*(b-1)

def modul(a,b):
    return a*b

def NWD(a,b):
    temp = 0
    while b!=0:
        temp = b
        b = a%b
        a = temp
    return a


# In[ ]:





# In[5]:


def mod1(number, phi):
    for i in range(2,phi):
        if (i*number)%phi == 1:
            return i


# In[6]:


def Zaszyfruj():
    wyk = int(input("Podaj wykladnik: "))
    modul = int(input("Podaj modul: "))
    f = "/home/users/dawid.bednarczyk/szyfr.txt" #input("Podaj plik do zaszyfrowania: ")
    s = "/home/users/dawid.bednarczyk/szyfr1.txt" #input("Podaj plik wyjsciowy: ")
    file1 = open(f, "r")
    #file2 = open(s, "x")
    file2 = open(s, "w")
    for line in file1:
        for letter in line:
            l=encrypt_RSA(letter, wyk, modul)
            file2.write(str(l))
            file2.write('\n')
        l=encrypt_RSA('\n', wyk, modul)
        file2.write(str(l))
        file2.write('\n')
    file1.close()
    file2.close()
    return "Zaszyfrowano"


# In[7]:



###porzucona!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def encrypt_RSA1(l,w,m):
    wyn = 1
    if type(l)==int:
        pot = l
    else:
        pot = ord(l)
    while w>0:
        if w%2==1:
            wyn = (wyn * pot) % m
        pot = (pot * pot) % m
        w=w/2
    return wyn


# In[8]:


def encrypt_RSA(i,w,m):
    return(ord(i)**w)%m


# In[9]:


def Deszyfruj():
    wyk = int(input("Podaj wykladnik: "))
    modul = int(input("Podaj modul: "))
    f = "/home/users/dawid.bednarczyk/szyfr1.txt" #input("Podaj plik do odszyfrowania: ")
    s = "/home/users/dawid.bednarczyk/szyfr2.txt" #input("Podaj plik wyjsciowy: ")
    file1 = open(f, "r")
    #file2 = open(s, "x")
    file2 = open(s, "w")
    for line in file1:
        l=decrypt_RSA(line,wyk,modul)
        #print(l)
        file2.write(chr(l))
    file1.close()
    file2.close()
    return "Odszyfrowano"


# In[10]:



#porzucona!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def decrypt_RSA1(a,w,m):
    wyn=1
    pot=int(a)
    while w>0:
        if w%2 == 1:
            wyn = (wyn * pot % m)
        pot = (pot*pot % m)
        w=w/2
    return wyn


# In[11]:


def decrypt_RSA(i,w,m):
    return (int(i)**w)%m


# In[12]:


def main():
    choice = 4
    while choice!=0:
        print("0 - zakoncz")
        print("1 - generuj klucze")
        print("2 - zaszyfruj plik")
        print("3 - deszyfruj plik")
        choice = int(input("Co chcesz zrobić?: "))
        if choice == 0:
            break
        elif choice == 1:
            print(genKeys())
        elif choice == 2:
            print(Zaszyfruj())
        elif choice == 3:
            print(Deszyfruj())


# In[15]:


genKeys()


# In[16]:


Zaszyfruj()


# In[17]:


Deszyfruj()


# In[13]:


main()


# In[ ]:





# In[ ]:


##/home/users/dawid.bednarczyk/szyfr.txt
##/home/users/dawid.bednarczyk/szyfr1.txt

