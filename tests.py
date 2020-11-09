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
    generator.shuffle(number)
    Pass="".join(number)
    try:
        Answer=passwordTester(Pass)
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
    return Answer

def PassGenerator_M1():
    global group6,group7,group8,group9,group10
    generator = Random()
    PassLen=generator.choice(range(8, 21))
    number = []
    number.append(generator.choice(group6))
    number.append(generator.choice(group6))
    number.append(generator.choice(group7))
    number.append(generator.choice(group8))
    number.append(generator.choice(group9))
    i=5
    while i<(PassLen+1):
        number.append(generator.choice(group10))
        i=i+1
    generator.shuffle(number)
    Pass="".join(number)
    try:
        Answer=passwordTester(Pass)
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
    return Answer

def PassGenerator_M2():
    global group6,group7,group8,group9,group10
    generator = Random()
    PassLen=generator.choice(range(8, 21))
    number = []
    number.append(generator.choice(group6))
    number.append(generator.choice(group6))
    number.append(generator.choice(group6))
    number.append(generator.choice(group7))
    number.append(generator.choice(group8))
    number.append(generator.choice(group9))
    i=6
    while i<(PassLen+1):
        number.append(generator.choice(group10))
        i=i+1
    generator.shuffle(number)
    Pass="".join(number)
    try:
        Answer=passwordTester(Pass)
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
    return Answer

def PassGenerator_M3():
    global group6,group7,group8,group9,group10
    generator = Random()
    PassLen=generator.choice(range(8, 21))
    number = []
    number.append(generator.choice(group6))
    number.append(generator.choice(group6))
    number.append(generator.choice(group6))
    number.append(generator.choice(group6))
    number.append(generator.choice(group7))
    number.append(generator.choice(group8))
    number.append(generator.choice(group9))
    i=7
    while i<(PassLen+1):
        number.append(generator.choice(group10))
        i=i+1
    generator.shuffle(number)
    Pass="".join(number)
    try:
        Answer=passwordTester(Pass)
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
    return Answer

class Test(unittest.TestCase):
    def test_ran1(self):
      i=0
      while(i<10):
        Ans1=PassGenerator_M()
        i=i+1
        print(Ans1)
      if (Ans1==False):
        Ans1=PassGenerator_M1()
        if (Ans1==False):
            Ans1=PassGenerator_M2()
            if (Ans1==False):
                Ans1=PassGenerator_M3()
                if (Ans1==False):
                    fi=open("Pass.txt","r")
                    line1=fi.readline()
                    fi.close()
                    Ans1=passwordTester(line1)
                    print(Ans1)
    def test_ran2(self):
      i=0
      while(i<10):
        Ans1=PassGenerator_M()
        i=i+1
        print(Ans1)
      if (Ans1==False):
            Ans1=PassGenerator_M1()
            if (Ans1==False):
                Ans1=PassGenerator_M2()
                if (Ans1==False):
                    Ans1=PassGenerator_M3()
                    if (Ans1==False):
                        fi=open("Pass.txt","r")
                        line1=fi.readline()
                        fi.close()
                        Ans1=passwordTester(line1)
                        print(Ans1)
    def test_ran3(self):
      i=0
      while(i<10):
        Ans1=PassGenerator_M()
        i=i+1
        print(Ans1)
      if (Ans1==False):
            Ans1=PassGenerator_M1()
            if (Ans1==False):
                Ans1=PassGenerator_M2()
                if (Ans1==False):
                    Ans1=PassGenerator_M3()
                    if (Ans1==False):
                        fi=open("Pass.txt","r")
                        line1=fi.readline()
                        fi.close()
                        Ans1=passwordTester(line1)
                        print(Ans1)

    def test_ran4(self):
      i=0
      while(i<10):
        Ans1=PassGenerator_M()
        i=i+1
        print(Ans1)
      if (Ans1==False):
            Ans1=PassGenerator_M1()
            if (Ans1==False):
                Ans1=PassGenerator_M2()
                if (Ans1==False):
                    Ans1=PassGenerator_M3()
                    if (Ans1==False):
                        fi=open("Pass.txt","r")
                        line1=fi.readline()
                        fi.close()
                        Ans1=passwordTester(line1)
                        print(Ans1)

    def test_ran5(self):
      i=0
      while(i<10):
        Ans1=PassGenerator_M()
        print(Ans1)
        i=i+1
      if (Ans1==False):
            Ans1=PassGenerator_M1()
            if (Ans1==False):
                Ans1=PassGenerator_M2()
                if (Ans1==False):
                    Ans1=PassGenerator_M3()
                    if (Ans1==False):
                        fi=open("Pass.txt","r")
                        line1=fi.readline()
                        fi.close()
                        Ans1=passwordTester(line1)
                        print(Ans1)
    def tests_a2(self):
      i=0
      while(i<10):
        Ans1=PassGenerator_M()
        print(Ans1)
        i=i+1
      if (Ans1==False):
            Ans1=PassGenerator_M1()
            if (Ans1==False):
                Ans1=PassGenerator_M2()
                if (Ans1==False):
                    Ans1=PassGenerator_M3()
                    if (Ans1==False):
                        fi=open("Pass.txt","r")
                        line1=fi.readline()
                        fi.close()
                        Ans1=passwordTester(line1)
                        print(Ans1)
if __name__ == '__main__':
    unittest.main()   