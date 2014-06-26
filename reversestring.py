import sys

## This program takes a string and reverses it

## Function to reverse string

def reverse(input, l):
	global output
	output = ""
	for x in range(0,l):
		output = output + input[(l-1)-x]
	print str(output)

## Main function
def main():
	string = raw_input('Input a string to be reversed: ')
	length = len(string)
	reverse(string, length)
	
main()