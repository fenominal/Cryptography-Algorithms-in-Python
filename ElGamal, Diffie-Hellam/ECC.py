# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 01:34:51 2018

@author: prem chand avanigadda
"""
#x^3+x+6, so a=1,b=6
a = 1
#b = 6

def inverseofNum(x,m):
    x = x%m
    for i in range(1,m):
        if((x*i)%m==1):
            return i
    return 1

def doublePoint(x,y):
    s = (inverseofNum(2*y,1039)*(3*(x**2)+a))%1039
    #print(s)
    x_res = ((s**2) - 2*x)%1039
    y_res = ((s*(x-x_res)) - y)%1039
    #print(x_res,y_res)
    return (x_res,y_res)

def largestpoint(l):
    l_x=0
    l_y=0
    for t in l:
        x,y = t[0],t[1]
        if(x>l_x):
            l_x,l_y = x,y
        elif(x==l_x):
            if(y>l_y):
                l_x,l_y = x,y
    return (l_x,l_y)

def multiplication(alpha,k):
    #ka or adding a for k times
    temp=alpha
    for i in range(k):
        x,y=addition(alpha,temp)
        temp=(x,y)
    return temp
        
def addition(p,q):
    s=((p[1]-q[1])*inverseofNum((p[0]-q[0]),1039))%1039
    x_r = ((s**2)-p[0]-q[0])%1039
    y_r = ((s*(p[0]-q[0]))-p[1])%1039
    return x_r,y_r
        
def findb(alpha,beta):
    i=0
    loopc=""
    temp = alpha
    while(loopc!="quit"):
        i=i+1
        temp=doublePoint(temp[0],temp[1])
        if(temp[0]==beta[0] and temp[1]==beta[1]):
            loopc="quit"
            return i
        
def elgamalEncryption(alpha,beta):
    print("Enter plain text")
    x_p=int(input("x in plaintext:"))
    y_p=int(input("y is plaintext:"))
    k=100
    y1 = multiplication(alpha,k)
    x,y = addition((x_p,y_p),multiplication(beta,k))
    y2 = (x,y)
    return (y1,y2)

def elgamalDecyption(alpha,beta):
    b=findb(alpha,beta)
    print("b value",b)
    k=100
    x_y1 = int(input("enter x in y1 cipher:"))
    y_y1 = int(input("enetr y in y1 cipher:"))
    x_y2 = int(input("enter x in y2 cipher:"))
    y_y2 = int(input("enetr y in y2 cipher:"))
    x_res,y_res = addition((x_y2,y_y2),multiplication((x_y1,-y_y1),k))
    return (x_res,y_res)
    
    
    
    
if __name__ == "__main__":
    x = int(input("x in alpha:"))
    y = int(input("y in alpha:"))
    m,l = x,y
    p = [(x,y)]
    loopc=""
    i=0
    while(loopc!="quit"):
        i=i+1
        pr = doublePoint(x,y)
        x,y = pr[0],pr[1]
        if(m==x and l==y):
            loopc = "quit"
            print("1. number of points: ",len(p))
        else:
            p.append(pr)
    print("2. largest point: ",largestpoint(p))
    print("3. is (1014, 291) belong to E: ",'Yes' if((1014.0, 291.0) in p) else 'No')
    loopc=""
    x_b = int(input("x in beta:"))
    y_b = int(input("y in beta:"))
    while(loopc!="quit"):
        print(" ElGamal public key")
        print("1.encryption")
        print("2.decryption")
        print("3.quit")
        choice = int(input("Enter choice:"))
        if(choice==1):
            print("encrypted result",elgamalEncryption((x,y),(x_b,y_b)));
        elif(choice==2):
            print("decrypted result",elgamalDecyption((x,y),(x_b,y_b)));
        elif(choice==3):
            loopc="quit"
        else:
            print("enter correct choice")
    print("Diffie-hellman key exchange")
    alpha_x = int(input("enter x in alpha:"))
    alpha_y = int(input("enter y in alpha:"))
    a_x = int(input("enter x in A:"))
    a_y = int(input("enter y in A:"))
    b_x = int(input("enter x in B:"))
    b_y = int(input("enter y in B:"))
    a_val = findb((alpha_x,alpha_y),(a_x,a_y))
    #b_val = findb((alpha_x,alpha_y),(b_x,b_y))
    #key = multiplication((a_x,a_y),b_val)
    #print(key)
    print(multiplication((b_x,b_y),a_val))
    
