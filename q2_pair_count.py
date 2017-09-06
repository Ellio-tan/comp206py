#!/usr/bin/python

import sys
import string
import operator
import os.path
from itertools import cycle 
testList = []
check = 0
if len(sys.argv) != 2 or os.path.isfile(sys.argv[1]) == False:
	print('Please enter two arguments with the file as the second')


else:	#print(sys.argv[1])
	dictList = {}
	with open(sys.argv[1], 'r') as f:
		for line in f: #Search through lines
			splitLines = line.split()
			
			
			for word in splitLines: #Search through lines 
				testList.append(word) #Add words to testList 

		licycle = cycle(testList)#Create iterable 
		nextWord = licycle.next()

		for y, x in enumerate(testList): #move through testList 
				x, nextWord = nextWord, licycle.next()#set next word 
				x = x.lower()
				nextWord = nextWord.lower()
					
				if testList[y] == testList[len(testList)-1]:#If it is the last word, end the seequence 
					break
				else:
					if (x.isalpha() is False):#check for symbols 
						for char in x:
							if char.isalpha() is False:
								x = x.translate(None, char) #Remove symbols 
					if (nextWord.isalpha() is False): #Do the same for nextWord 
						for char in nextWord:
							if char.isalpha() is False:
								nextWord = nextWord.translate(None, char)
				
					wordCombo = x + "-" + nextWord #combine words 
			
					if dictList.has_key(wordCombo): #Add/update value 
						dictList[wordCombo] += 1
					else:
						dictList[wordCombo] =1
		
				#testList[:] = []


	for frequency in sorted(dictList.items(), key = lambda x:x[1], reverse=True):#print 
		print frequency[0], ":", frequency[1]
	
	f.close() #Close file 
	

