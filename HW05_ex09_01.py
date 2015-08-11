#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def long_words():
	try:
		fin = open('words.txt')
		line = fin.readline()
		for line in fin:
			s = line.split()
			for i in range (len(s)):
				if len(s[i]) > 20:
					print s[i]
						
	except:
		print 'Something went wrong with the file'
	


##############################################################################
def main():
	# Call your functions here.
	long_words()

if __name__ == '__main__':
    main()
