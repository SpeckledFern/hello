# Author: Sierra Freihoefer
# Date: 1-13-2021
# Description: Given a year this program will tell you if its a leap year

#IN ORDER TO RUN
#Use python3, such as
#     python3 sierra_freihoefer_hw1.py
# Then enter the year of your choice

print("Leap Year Check\n")
inp = input("Enter a year: ")

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

