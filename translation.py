################################
# File Name: translation.py
# Author:    Bryan Stander
# Date:		 5/7/15
# Class:	 Capstone
# Purpose:	 The purpose of this assignment is to read in string of 
# 			 DNA strands and create a codex out of them using known phrases in the code.
################################

#Quotes in the strands
QUOTE1 = '"TO LIVE, TO ERR, TO FALL, TO TRIUMPH, TO RECREATE LIFE OUT OF LIFE"'
QUOTE2 = '"SEE THINGS NOT AS THEY ARE, BUT AS THEY MIGHT BE"'
QUOTE3 = '"WHAT I CANNOT BUILD, I CANNOT UNDERSTAND."'
RESTRICTION_SITE = "TTAACTAGCTAA"



f = open("watermarks.txt")
decodedFile = open("DecodedStrings.txt", 'w')

g = f.read()
#Breaks the one string up into "four" different pieces.
junk,strand1,junk,strand2,junk,strand3,junk,strand4,junk = g.split(RESTRICTION_SITE)
#remove all newline characters
strand1 = strand1.replace('\n', '')
strand2 = strand2.replace('\n', '')
strand3 = strand3.replace('\n', '')
strand4 = strand4.replace('\n', '')
#test to make sure the strings are all there
print len(strand1) 
print len(strand2)
print len(strand3)
print len(strand4)

#uses a codex to find what is written a given strand
def decode_strand(codex, strand):
	decodeStrand = iter(strand)
	loop = True
	while loop is True:
		try:
			codon = str(decodeStrand.next()) + str(decodeStrand.next()) + str(decodeStrand.next())
		except StopIteration:
			loop = False
		if codex.has_key(codon): 
			print codex.get(codon) ,
		else:
			#print  codon,
			print codon ,
	print ""
	
	
#write to a file instead of the screen	
def print_strand(codex, strand):
	decodeStrand = iter(strand)
	loop = True
	while loop is True:
		try:
			codon = str(decodeStrand.next()) + str(decodeStrand.next()) + str(decodeStrand.next())
		except StopIteration:
			loop = False
		if codex.has_key(codon): 
			decodedFile.write( codex.get(codon) )
		else:
			#print  codon,
			decodedFile.write('?')
	print ""
	
#initial codex creation: takes in a strand, a blank codex, and a quote. 	
def find_codex(codex, strand, quote):
	test = True
	done = False
	for x in range (0, len(strand)):
		if done is False:
			y = 0;
			currentStrand = iter(strand)
			for z in range(0, x):
				currentStrand.next()
			currentQuote = iter(quote)
			while test is True:
				codon = str(currentStrand.next()) + str(currentStrand.next()) + str(currentStrand.next())
				try:
					letter = str(currentQuote.next())
					if codex.has_key(codon):
						if codex.get(codon) is not letter:
							test = False
							codex.clear()
						else:
							print codex.get(codon),
					else:
						codex[codon] = letter
						print codex.get(codon),
				except StopIteration:
					print"Codex found"
					print codex
					done = True
					test = False
				
			test = True
			print 
#Prints codex to the screen			
def print_codex(codex):
	for x in codex:
		print(x),
		print '=',
		for y in codex[x]:
			print y
#Adds a character to codex manually. 
def add_character(codex):
	key = raw_input ('Enter Codon: ')
	letter = raw_input ('Enter Letter: ')
	codex[key] = letter
#Does nothing, was a nice idea, but never needed
def delete_character(codex):
	pass
	
#Main editing loop of the program. Allows the user to edit, print, and change strands to work on
def edit (codex, strand):
	choice = 0
	choice2 = 0
	while choice is not 6:
		print "Please Select an option: "
		print "1: add character"
		print "2: print codex"
		print "3: print string"
		print "4: change string"
		print "5: print to file"
		print "6: done"
		try:
			choice = input(":")
			print choice
			while choice  < 1 or choice > 6:
				choice = input("That is not a valid option \nPlease select again: ")
		except SyntaxError:
			choice = 0
		if choice is 1:
			add_character(codex)
		elif choice is 2:
			print_codex(codex)
		elif choice is 3:
			decode_strand(codex, strand)
			
		elif choice is 4:
			choice2 = input ("Which string?: ")
			if choice2 is 1:
				strand = strand1
			elif choice2 is 2:
				strand = strand2
			elif choice2 is 3:
				strand = strand3
			elif choice2 is 4:
				stand = strand4
			else:
				print "Invalid string"
				
		elif choice is 5:
			print_strand(codex, strand)
		elif choice is 6:
			pass
		else:
			pass
		

			
#initialize 	
codex1 = {}
codex2 = {}
codex3 = {}
codexCombine = {}

#Makes a codex out of each quote and corresponding strand then combines them into one.
find_codex(codex1, strand2, QUOTE1)
print_codex(codex1)
decode_strand(codex1, strand1)
find_codex(codex2, strand4, QUOTE3)
find_codex(codex3, strand3, QUOTE2)
print_codex(codex1)
print_codex(codex2)
codexCombine = codex1.copy()
codexCombine.update(codex2)
codexCombine.update(codex3)
decode_strand(codexCombine, strand4)
#allows you to see the combined codex, created without user input. 
print
print_codex(codexCombine)
#prints the last strand after being ran through decoder. 
print
decode_strand(codexCombine, strand4)
#allows for user to mess around with it manually. 
edit(codexCombine, strand2)
decodedFile.close()
	
	
	


	
				 




