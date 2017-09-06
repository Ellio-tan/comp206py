#!/usr/bin/python

import sys
import string
import operator 
import os.path
if len(sys.argv) != 2 or os.path.isfile(sys.argv[1]) == False:
	print('Please enter two arguments with the file as the second')
else: 
	#print(sys.argv[1])
	dictList = {}
	with open(sys.argv[1], 'r') as f:
		for line in f: #Search through lines
			
			for word in line.split(): #Search through lines 
				word = word.lower() #put words to lowercase 
				if '-' in word: #split up hyphen
					splitwords = word.split('-')

					for splitWord in splitwords: 
						for char in splitWord: #Check for other symbols/ remove the hyphen 
							if char.isalpha() is False:
								splitWord = splitWord.translate(None, char)
							if dictList.has_key(splitWord):
								dictList[splitWord] += 1
							else:
								dictList[splitWord] = 1
					continue

				if word.isalpha() is False: #Check if the word contains numbers of symbols 
					for char in word:
						if char.isalpha() is False:
							word = word.translate(None, char) #remove the word 
					
					if dictList.has_key(word): #Add word to dictionary 
						dictList[word] += 1
					
					else:
						dictList[word] = 1
					
				
				if dictList.has_key(word): #no change necessary, add word to dictionary 
					dictList[word] += 1
					
				else:
					dictList[word] = 1
				
			
	
		
	for frequency in sorted(dictList.items(), key = lambda x:x[1], reverse=True):
		print frequency[0], ":", frequency[1]
	print len(dictList)
	f.close()
	

