#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
	""" Is it a good practice to write code in try other than the required code to be tried
	for exception? If not, how do we achieve the same without writing in try? Using function 
	calls from within try with the function having the even/odd check in this case?
	"""
	num = raw_input("Enter a number: ")
	try:
		int_num = int(num)
		if int_num % 2 == 0:
			print "even number"
		else:
			print "odd number"
	except:
		print "Enter a integer this time..."
		even_odd()
		
	


def ten_by_ten():
	""" Prints integers 1 through 100 sequentially in a ten by ten grid."""
	for i in range (1,101):
		if i < 10:
			print i,"",
		elif i % 10 != 0:
			print i,
		else:
			print i,"\n"

def find_average():
	""" Takes numeric input (non-word numerals) from the user, one number
	at a time. Once the user types 'done', returns the average.
	"""
	count = 0
	sum = 0
	while True:
		num = raw_input("Enter the numbers to be averaged. Say 'done' after you entered all the numbers: ")
		try:
			int_num = int(num)
			sum += int_num
			count += 1
		except:
			if num == "done":
				break
			else:
				print "Only enter numbers..."
	count = count * 1.0
	average = sum/count
	return average

	
	
##############################################################################
def main():
	even_odd()
	ten_by_ten()
	print find_average()
if __name__ == '__main__':
    main()
""" Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """