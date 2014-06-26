import sys

##Notes:
##sys.argv[0] refers to the main function. 1,2,3 etc refer to arguments after that. Useful if want to input known values.
##If want value from user, use raw_input() to get information and store as variable. Ex:
## var = raw_input('Prompt goes here')
##print var

def mult():
	answer = int(sys.argv[2])*int(sys.argv[3])
	print str(answer)

def main():
	print 'Hello there', sys.argv[1]
	mult()
	name = raw_input('Please input something: ')
	print 'You will love this,', name
	

if __name__ == '__main__':
	main()