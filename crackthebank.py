from random import randint
from time import time

print """

#############################
#                           #
#    Crack The Bank Game    #
#                           #
#    Twitter: KendoClaw1    #
#############################




"""
print "Welcome to crack the bank game"
print "Your goal is to find the correct digits to crack the bank safe"
print "Please choose a difficulty"
print "1-Easy (3 digits code)"
print "2-Medium (5 digits code)"
print "3-Hard (7 digits code)"
choice = raw_input("> ")

def start():
	print "1-Easy (3 digits code)"
	print "2-Medium (5 digits code)"
	print "3-Hard (7 digits code)"

	choice = raw_input("> ")


def level1():
	code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
	guess = raw_input("Keypad> ")
	starttime = time()
	while guess != code:
		if guess > code:
			print "LOWER"
		elif guess < code:
			print "HIGHER"
		guess = raw_input("Keypad> ")

	if guess == code:
		endtime = time()
		print " Congratulations, you cracked the safe!"
		print 'Total Time:', round(endtime - starttime, 2),'secs'

def level2():
	code = "%d%d%d%d%d" % (randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9))
	guess = raw_input("Keypad> ")
	starttime = time()
	while guess != code:
		if guess > code:
			print "LOWER"
		elif guess < code:
			print "HIGHER"
		guess = raw_input("Keypad> ")

	if guess == code:
		endtime = time()
		print " Congratulations, you cracked the safe!"
		print 'Total Time:', round(endtime - starttime, 2),'secs'

def level3():
	code = "%d%d%d%d%d%d%d" % (randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9))
	guess = raw_input("Keypad> ")
	starttime = time()
	while guess != code:
		if guess > code:
			print "LOWER"
		elif guess < code:
			print "HIGHER"
		guess = raw_input("Keypad> ")

	if guess == code:
		endtime = time()
		print " Congratulations, you cracked the safe!"
		print 'Total Time:', round(endtime - starttime, 2),'secs'

try:
	if choice == "1":
		level1()
	elif choice == "2":
		level2()
	elif choice == "3":
		level3()
	else:
		print "please choose a difficulty ..."
		start()
except KeyboardInterrupt:
	print "\nBye"