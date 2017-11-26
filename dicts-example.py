#!/usr/bin/python
#I made this script to practice using dicts :)

cities = {'CA':'San fran','MI':'Detroit','FL':'Jacksonville'}
cities['NY'] = 'new york'
cities['OR'] = 'Portland'

def find_city(themap,state):
	if state in themap:
		return themap[state]

	else:
		return "Not found"

def addcity():
	while True:
		key = raw_input("Enter the City key:\n> ")
		city = raw_input("Enter the City:\n> ")
		cities.setdefault(key,city)
		whattodo = raw_input("To return to main menue type 1\nto quit press enter")
		if whattodo == '1':
			main()
			break
		else:
			break


#PAY ATTENTION
def app():
	cities['_find'] = find_city


	while True:
		state = raw_input("State? (Enter to return to main menue)\n> ")
		if not state:
			main()
			break
		# this line is the most important ever! study!
		city_found = cities['_find'](cities, state)
		print city_found

def main():
	print "Welcome to the map.\n if u want to view your current map type 1\n if u want to add stuff to the current map type 2\n if u want to search cities in the current map press 3."
	choice =  raw_input("(press enter to exit) > ")
	if choice == '1':
		for key,city in cities.items():
			print key,city
		print "\n\n"
		main()
	elif choice == '2':
		addcity()
	elif choice == '3':
		app()
	elif not choice: exit()
	else:
		print "can't you read??"
		main()
try:
	main()
except:
	print "\nSomething wrong happened, run the script again"
