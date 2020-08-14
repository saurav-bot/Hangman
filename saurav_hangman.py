# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:38:57 2020

@author: Saurav Pandey
"""
import random
from os import system

def insert(guess,l):
    ''' Find position to where are words and insert them'''
    pos=[]
    guess= list(guess)
    for i in range(len(word)):
        if word[i]==l:
            pos.append(i)
    for i in pos:
        guess[i]=word[i]
    guess="".join(guess)
    return guess

def start():
    fruits=['apple','banana','kiwi','strawberry','mango','lichi','guava']
    word=random.choice(fruits)
    print("Guess the name of fruit\n")
    print(f"You have only {len(word)+2} chances!\t")
    # for i in range(len(word)):
    #     print("-",end='')
    print('-'*len(word))
    print()
    

    return word
 
def validating_input(word):
    ''' Validate length of input , is it digit or not ,
    then check is this letter present in word'''

    guess="-"*len(word)
    length=len(word)+2
    while length>=0:
        l=input("Enter a letter only: ")
        if l==l.isalpha():
            print("Enter only letters")
            length=length-1
        elif l not in word:
            print("Not in word")
            length=length-1
        elif l in word:
            guess=insert(guess,l)
            print(guess)
        if guess==word:
            print("You are right")
            print("The world is :",guess)
            print("Congratulation!!! :)")
            break

if __name__ =="__main__": 
    while True:  
        print() 
        print("---- Welcome to Hangman ----")
        print()
        word= start() 
        validating_input(word)    
        i = input("Do you want to play again ? Y/n:\t")
        if i.lower() == 'n':
            break 
        else:
            system('cls')
    

   


