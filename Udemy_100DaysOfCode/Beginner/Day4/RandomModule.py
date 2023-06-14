#always a good choice to refer to the documentation
#https://docs.python.org/3/library/random.html

#random(), which generates a random float uniformly in the semi-open range [0.0, 1.0).
#Python uses the Mersenne Twister as the core generator. 
#It produces 53-bit precision floats and has a period of 2**19937-1. 
#The underlying implementation in C is both fast and threadsafe. 
#The Mersenne Twister is one of the most extensively tested random number generators in existence. 
#However, being completely deterministic, it is not suitable for all purposes, and is completely unsuitable for cryptographic purposes.

#psedo random generators on Khan academy for better understanding of number generators. 

#to use to the various functions included in random module, we have to import the module first.
import random 

