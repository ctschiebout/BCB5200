#!/usr/bin/env python
import os, sys, re

def reverse(s):
    
    return s[::-1]

def complement(s):

    base_complementary= {'A':'T','T':'A','G':'C','C':'G','a':'T','t':'A','g':'C','c':'G'}
    rev_list=reverse(s)
    listf = [(base_complementary[char]) for char in rev_list]
    return "".join(listf)

def main():

    dna_seq = raw_input('Type your DNA sequence : ')

    for letter in dna_seq:
        if letter not in "ATGCatgc":
            print "** Error: Not a DNA sequence"
            sys.exit()

    print "Reverse complement DNA :", complement(dna_seq)
    sys.exit()

if __name__ == '__main__': main()
