#!/usr/bin/env python


mod = 256 
def initialise(key): 
    s=[]
    if len(key)<5 : 
        print("Please insert a key +5 chars") 
    else : 
        for i in range(mod) : 
            s.append(i) 
        j=0
        for i in range(mod) : 
            j = (j+s[i]+ord(key[i%len(key)])) % mod 
            s[i], s[j] = s[j], s[i] 
    return s
    
def keyStream(s,l) : 
    i=0
    j=0 
    for m in range(l) : 
        i = (i+1) % mod 
        j = (j+s[i]) % mod 
        s[i], s[j] = s[j] , s[i] 
  #  print(s[(s[i]+s[j]) % mod])
    return s[(s[i]+s[j]) % mod]

def algo(msg ,key):
    result="" 
    for c in msg :
        res = ord(c)^keyStream(initialise(key),len(msg))
        result= result +chr(res)
    return result 
     

def main():
    print('Welcome to the rc4 algorithm !')
    print('Prove yourself to the algorithm and the algorithm will reward you !!')
    while True:
        try:
            key = input("key : ")
            if key == 'end':
                return
            msg = input("your msg :")
            enc = algo(msg,key)
            print(">> ", end="")
            print(enc)
        except ValueError:
            print("Invalid input. ")

if __name__ == '__main__':
    main()
