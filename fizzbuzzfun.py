""" 
Title: FizzBuzzFun
Author: Madeline Seifert
Created: 8/18/2023

The goal of FizzBuzz is to print the numbers in a range except if the number is divisible by 3, print "Fizz" and if the number is divisible by 5, print "Buzz". If the number is divisible by both, print "FizzBuzz". 
"""


"""classic FizzBuzz with for loops
   num- an int of how many numbers to print (inclusive)"""
def FizzBuzz(num):
	for i in range(1,num+1):
		if i % 3 == 0 and i % 5 == 0:
			print("FizzBuzz ") #space btwn nums included in str
		elif i % 3 == 0:
			print("Fizz ")
		elif i % 5 == 0:
			print("Buzz ")
		else: print(i)
		


"""FizzBuzz by concatenating everything into a str
   num- an int of how many numbers to print (inclusive) """
def FizzBuzzStr(num):
	fuzz = '' #str that will be printed at the end
	for i in range(1, num+1): #range is 1-num inclusive
		if i % 3 == 0:
			fuzz += "Fizz"
		if i % 5 == 0: #if so that checks if num is ALSO div by 5 
			fuzz += "Buzz"
		elif i % 3 > 0: #here b/c if num is div by 3, will also add the num if this was an else statement
			fuzz += str(i)
		fuzz += " " 
	print(fuzz)



"""FizzBuzz using recursion, printing all in one str
   num- an int of how many numbers to print (inclusive)
   fuzz- dont need to enter anything, str that will be printed """
def FizzBuzzRec(num, fuzz = ''):
	if num < 1: 
		print(fuzz)
	elif num % 3 == 0 and num % 5 == 0:
		return FizzBuzzRec(num-1, "FizzBuzz "+fuzz)
	elif num % 3 == 0:
		return FizzBuzzRec(num-1, "Fizz "+fuzz)
	elif num % 5 == 0:
		return FizzBuzzRec(num-1, "Buzz "+fuzz)
	else:
		return FizzBuzzRec(num-1, str(num)+" "+fuzz)

