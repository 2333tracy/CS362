#!/usr/bin/python
from random import Random
import unittest
import os
import time

group1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
group2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
group3 = ['0','1','2','3','4','5','6','7','8','9']
group4 = ['~',r'\'','!','@','#','$','%','^','&','*','(',')','_','+','-','=']
group5 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','~',r'\'','!','@','#','$','%','^','&','*','(',')','_','+','-','=']

def PassGenerator():
    global group1,group2,group3,group4,group5
    generator = Random()
    PassLen=generator.choice(range(8, 21))
    number = []
    number.append(generator.choice(group1))
    number.append(generator.choice(group2))
    number.append(generator.choice(group3))
    number.append(generator.choice(group4))
    i=4
    while i<(PassLen+1):
        number.append(generator.choice(group5))
        i=i+1
    Pass="".join(number)
    return Pass

def writeFile():
    PassW=PassGenerator()
    ofs = open("Pass.txt","w")
    ofs.write(PassW)
    ofs.close()

def check_pwd(n):
    global group1,group2,group3,group4,group5
    if os.path.exists('Pass.txt'):
        try:
            f=open("Pass.txt","r")
            line=f.readline()
            f.close()
            if str(n)==str(line):
                os.remove('Pass.txt')
                return True
            else:
                return False
        except Exception as error:
            return error
    else:
            writeFile()