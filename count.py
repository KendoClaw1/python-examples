from sys import argv

def main(): 
	num = argv[1]
	limit = argv[2]
	save_to = argv[3]
	numi= int(num)
	limiti = int(limit)
	file1 = open(save_to,'w')
	while numi < limiti:
		file1.write(str(numi))
		file1.write("\n")
		numi += 1
	print "Done,numbers saved to " + argv[3] + " :)"
		
try:
	main()
except IndexError:
	print(" Something wrong happened\nUsage: python "+ argv[0]+" count.py 1 10 numbers.txt\n")
 
	

	
	
