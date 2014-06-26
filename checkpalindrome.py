import sys

## Checks if string is a palindrome

## Reverses string
def reverse(string, length):
	global check
	check = ""
	for x in range(0, length):
		check = check + str(string[(length-1)-x])
	return check

## Compares string to reversed string
def compare(string):
	l = len(string)
	global palindrome
	palindrome = False
	if string == str(reverse(string, l)):
		palindrome = True
	else:
		palindrome = False
	return palindrome

## Takes user input and passes to compare()
def main():
	s = raw_input("Enter string: ")
	if compare(s) == True:
		print str(s) + " is a palindrome."
	else:
		print str(s) + " is not a palindrome."
		
main()