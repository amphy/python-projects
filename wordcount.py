import sys

## This program counts the number of words from a text file and generates a summary.

## Reads the .txt file and counts the number of words.
def words(string):
	with open(string, "r") as myFile:
		data=myFile.read().replace("\n", "")
		dataArray = data.split(" ")
		return len(dataArray)

## Reads the .txt file and counts the number of characters.
def characters(string):
	with open(string, "r") as myFile2:
		data2=myFile2.read().replace("\n", "")
		return len(data2)

## Takes in user input and counts number of words.
def main():
	s = raw_input("Enter file name: ")
	print "Your file has " + str(words(s)) + " words and " + str(characters(s)) + " characters."

main()