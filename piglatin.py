import sys

## This program converts phrases to Pig Latin

## Check for first consonant sound
def cons(string):
	global counter
	counter = 0
	length = len(string)
	for x in xrange(length):
		if string[x] in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
			break
		else:
			counter+=1

# Converts word to Pig Latin
def transform(string):
	if counter > 0:
		transformation = str(string[counter:]) + str(string[:counter]) + "ay"
	else:
		transformation = str(string) + "way"
	return transformation

# Separates input string into list of words
def sep(string):
	global sentenceArray
	sentenceArray = string.split(" ")
	return len(sentenceArray)

# Execute translation
def main():
	s = raw_input("Enter a phrase to be translated to Pig Latin (Please leave out punctuation): ")
	global output
	output = ""
	for x in range(0,sep(s)):
		cons(sentenceArray[x])
		output = output + transform(sentenceArray[x]) + " "
	print output	
	
main()