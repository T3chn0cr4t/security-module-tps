1st Part : 
openssl rand -hex 128
Results : 
54d8dc0f33af766c9dee03fe4e76c44da0949c1e10ac45aec87bb0
c2fe6bb4fefd895a199d8ca80c3866230c068036d69b389ef8a3b4
d15ef428d6903aa93402bc0b6261e5487258641bb2c78de98fa3d5
ddbf2140e42e1e5c267c08c09b574e76ed7ee0322886ec37b24e5e
2e52edfbde5401e40b5ddba3a6811eaab1580ec5

2nd Part : 
openssl dgst -md5 -out hash openssl.md
Results : (strings hash)
MD5(openssl.md)= d41d8cd98f00b204e9800998ecf8427e

3rd Part : 
openssl enc -bf-ecb -in openssl.md -out openssl.chiffre 

Result : (encrypted & plaintext) files 

4th Part : 

