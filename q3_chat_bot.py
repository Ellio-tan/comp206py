#!/usr/bin/python

import sys
import string
import operator
import os.path
import random 
from itertools import cycle 

numArg = 1 #used to loop through arguments to check if they are files 
counter = 1 #used to loop through arguments to place into list #Different from numArg just for clairty, they do the same thing 
testList = []
comboList = []


for x in sys.argv[1:]:
	if os.path.isfile(sys.argv[numArg]): #Check if all arguments are files 
		numArg +=1 
		
	else:
		print "Please only enter in valid text files" 
		break

for x in sys.argv[1:]: #add files to list 
	with open(sys.argv[counter], 'r') as f: 
		for line in f:
			for word in line.split():
				word = word.lower() #Put words to lowercase
				if '-' in word: 
					splitwords = word.split('-')
					for splitword in splitwords:
						for char in splitword:
							if char.isalpha() is False:
								splitword = splitword.translate(None,char)
				
						testList.append(splitword)
				elif word.isalpha() is False:
					
					for char in word:
						if char.isalpha() is False:
							word = word.translate(None,char)
					testList.append(word)
					
				else: 
					testList.append(word)


	f.close()
	

	licycle = cycle(testList)
	next = licycle.next()
	for x, firstW in enumerate(testList): #Create combolist
		firstW, next = next, licycle.next()
		
		if testList[x] == testList[len(testList)-1]:
			break
		else: 
			firstW = firstW.lower()
			next = next.lower()
			if "." in firstW: 
				continue
			wordCombo = firstW + " " + next
			comboList.append(wordCombo)
			
	counter +=1 #iterate counter to get next file 

while (1): 
	userList = []
	userQ = raw_input("Send: ")
	lastWord = None #last word 
	firstWordList = [] #Generate list of pairs that contain the first word, in order to select a random one from it to create the first word 
	outList = []
	firstTruth = False 

	for word in userQ.split(): #Create list of words for user 
		userList.append(word)

	for x, word in enumerate(userList): #Get last word from list 
		if userList[x] == userList[len(userList)-1]:
			lastWord = word

	if lastWord.isalpha() is False: #Remove symbols from the last word (QN)
		for char in lastWord:
			if char.isalpha() is False:
				lastWord = lastWord.translate(None, char)	
	lastWord = lastWord.lower() 

	for item in comboList: #Check to see if last word is in the comboList 
		if item.find(lastWord) != -1:
			firstWordList.append(item)
			firstTruth = True 

	if firstTruth == True: #if last word is in the list 
		firstWord = random.choice(firstWordList)
		firstWord = firstWord.capitalize()
		
	else: 
		firstWord = random.choice(comboList)
		firstWord = firstWord.capitalize()

	
	outList.append(firstWord + " " ) #CONDITION ONE SATISFIED 
	
	
	while len(outList)<10:
		newWord = random.choice(comboList)	
		if "." in lastWord: #End statement if the first pair has a period 
			break

		if "?" in newWord: #if the word ends in ! or ? 
			newWord.replace("?", ".")
			outList.append(newWord)
			break

		if "!" in newWord:
			newWord.replace("!", ".")
			outList.append(newWord)
			break

		if "." in newWord: #STOP-PAIR CONDITiON
			outList.append(newWord)
			break

		if len(outList) == 9: #add period to the end if no period 
			outList.append(newWord)
			outList.append(".")
			#print "here"
			break

		outList.append(newWord + " " ) #add spaces 

	outListstr = ''.join(outList) #Join the list into one string 
	print "Receive: ", outListstr
	




	
