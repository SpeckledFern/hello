# Author: Sierra Freihoefer
# Date: 1-29-2021
# Description: Given a year this program will tell you if its a leap year, with error handling.

#IN ORDER TO RUN
#Use python3, such as
#     python3 leap_error_handling.py
# Then enter the year of your choice

bad = 1

while bad:
	seen = 0
	print("Leap Year Check\n")
	inp = input("Enter a year: ")
	#print(len(inp))
	for x in range(len(inp)):
		if inp[x] > '9' or inp[x] < '0':
			print("Error: input must be a whole number consisting of integers")
			seen += 1
			break;
	if seen > 0:
		bad = 1
	else:
		bad = 0
	
inp = int(inp)	
if inp%4 == 0:
	if inp%100 == 0:
		if inp%400 == 0:
			print(inp, " is a leap year")
		else: 
			print(inp, " is NOT a leap year")
	else:
		print(inp, " is a leap year");
else: 
	print(inp, " is NOT a leap year");

