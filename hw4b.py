#!/usr/bin/env python
import os, sys, re
from Bio.Seq import Seq

def main():

    dna_seq = (raw_input('Type your DNA sequence : '))
    # Seq object call
    revcomp = Seq(dna_seq)
    # call reverse_complement function in Bio.Seq
    dna_seq= revcomp.reverse_complement()
    # print output
    print "Reverse complement DNA :", dna_seq
    sys.exit()
    
if __name__ == '__main__': main()
