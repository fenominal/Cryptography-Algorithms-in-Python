# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:49:59 2018

@author: prem chand avanigadda
"""
ALPHABETS = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,
'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

def readFile():
    filename = input("Enter cipher file name to decrypt:")
    with open(filename,'r') as cipherfile:
        ciphertext = cipherfile.read().split("\n")
    return ciphertext

class ELGamal:
    def __init__(self,ciphertext,a,p):
        #split the cipher into y1 and y2
        self.y1 = ciphertext[0]
        self.y2 = ciphertext[1]
        self.a = a
        self.p = p
        
    def alphaChar(self,v):
        for key,val in ALPHABETS.items():
            if v==val:
                return key
        return 1

    def intToAlpha(self,n):
        #based on x*26^2 + y * 26 + z
        x = int(n/(26*26))
        temp = n-(x*26*26)
        y = int(temp/26)
        z = temp-(y*26)
        return self.alphaChar(x)+self.alphaChar(y)+self.alphaChar(z)
    def inverseofNum(self,x):
        x = x%self.p
        for i in range(1,self.p):
            if((x*i)%self.p==1):
                return i
        return 1
    def decrypt(self):
        # x = y2(y1^a)^-1 mod p
        temp = self.y1**self.a
        x = (self.y2*self.inverseofNum(temp))%self.p
        return self.intToAlpha(x)
if __name__ == "__main__":
    print("   ELGamal cryptosystem   ")
    a = int(input("Enter a:"))
    p = int(input("Enter p:"))
    alpha = int(input("Enter alpha val:"))
    plain = ""
    for cipher in readFile():
        temp = eval(cipher)
        ob = ELGamal(temp,a,p)
        plain += ob.decrypt().lower()
    print(plain)
