import sys

## This program counts the number of vowels in a string and reports the frequency of each vowel.

## Declare  and Define Global variables


## Counts the number of vowels and gives frequency
def count(string):
	global counter_a
	counter_a = 0
	global counter_e
	counter_e = 0
	global counter_i
	counter_i = 0
	global counter_o
	counter_o = 0
	global counter_u
	counter_u = 0
	global cons
	cons = 0
	length = len(string)
	for x in range(0, length):
		if string[x] in ("a", "A"):
			counter_a = counter_a + 1
		elif string[x] in ("e", "E"):
			counter_e = counter_e + 1
		elif string[x] in ("i", "I"):
			counter_i = counter_i + 1
		elif string[x] in ("o", "O"):
			counter_o = counter_o + 1
		elif string[x] in ("u", "U"):
			counter_u = counter_u + 1
		else:
			cons = cons + 1
	total = counter_a + counter_e + counter_i + counter_o + counter_u
	print "The total number of vowels in \"" + str(string) + "\" is " + str(total)
	print "The frequency of each: a=" + str(counter_a) + " e=" + str(counter_e) + " i=" + str(counter_i) + " o=" + str(counter_o) + " u=" + str(counter_u)


## Executes the count and frequency report
def main():
	s = raw_input("Enter a string to be counted: ")
	count(s)
	
main()