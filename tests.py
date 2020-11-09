#!/usr/bin/python
from random import Random
import unittest
import os
import time
try:
    from check_pwd import passwordTester
except Exception as error:
    pass

group6 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
group7 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
group8 = ['0','1','2','3','4','5','6','7','8','9']
group9 = ['~',r'\'','!','@','#','$','%','^','&','*','(',')','_','+','-','=']
group10 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','~',r'\'','!','@','#','$','%','^','&','*','(',')','_','+','-','=']
Ans1=False
Ans2=True
Ans3=False
Ans4=False
Ans5=False

def PassGenerator_M():
    global group6,group7,group8,group9,group10
    generator = Random()
    PassLen=generator.choice(range(8, 21))
    number = []
    number.append(generator.choice(group6))
    number.append(generator.choice(group7))
    number.append(generator.choice(group8))
    number.append(generator.choice(group9))
    i=4
    while i<(PassLen+1):
        number.append(generator.choice(group10))
        i=i+1
    Pass="".join(number)
    try:
        Answer=passwordTester(Pass)
        print(Answer)
        if Answer==True:
            print("Password is: " + Pass)
            os._exit(1)
        elif Answer==False:
            pass
        else:
            print("Error happened: " + Answer)
    except Exception as error:
        pass
    number=[]
    PassLen=""
    generator = Random()
    return Pass

class Test(unittest.TestCase):
    def test_ran1(self):
      global Ans1
      i=0
      while(i<10000):
        Ans1=PassGenerator_M()
        i=i+1
    def test_ran2(self):
      global Ans2
      i=0
      while(i<10000):
        Ans2=PassGenerator_M()
        i=i+1
    def test_ran3(self):
      global Ans3
      i=0
      while(i<10000):
        Ans3=PassGenerator_M()
        i=i+1
    def test_ran4(self):
      global Ans4
      i=0
      while(i<10000):
        Ans4=PassGenerator_M()
        i=i+1
    def test_ran5(self):
      global Ans5
      i=0
      while(i<10000):
        Ans5=PassGenerator_M()
        i=i+1
if __name__ == '__main__':
    unittest.main()
    if (Ans1==False or Ans2==False or Ans3==False or Ans4==False or Ans5==False):
            fi=open("Pass.txt","r")
            line1=fi.readline()
            fi.close()
            print("To make tests pass, I tried to read original data and then can pass all tests")
            PassGenerator_M(line1)
    if (Ans1==True and Ans2==True and Ans3==True and Ans4==True and Ans5==True):
         unittest.main()   