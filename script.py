#!/usr/bin/python3
# -*- coding: utf-8 -*-

f = open('palavras.txt', 'r')

def findWord(word):
    for i in f:
        if word in i:
            print(i)

if __name__ == "__main__":
    findWord("banana")
