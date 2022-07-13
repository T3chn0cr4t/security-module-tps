from Crypto.Util.number import getStrongPrime, inverse
from Crypto.Util.number import *
import hashlib, sys, os, signal, random


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

p = 1217
q = 1021

n= p*q 
phi= (p-1)*(q-1)
e = random.randrange(1, phi)
g = gcd(e, phi)
while True:
    #as long as gcd(1,phi(n)) is not 1, keep generating e
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    #generate private key
    d = mod_inverse(e, phi)
    print(e,d)
    if g == 1 and e != d:
        break
        print(e)
        public=(e,n)
        print(e)



    #public key (e,n)
    #private key (d,n)
public=(e,n)
private=(d,n)


def encrypt(msg_plaintext, package):
    #unpack key value pair
    e, n = package
    msg_ciphertext = [pow(ord(c), e, n) for c in msg_plaintext]
    print(msg_ciphertext)
    return msg_ciphertext

encrypt("helloworld",public)