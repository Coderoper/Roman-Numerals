#!/usr/bin/env python
import sys

values = [1,5,10,50,100,500,1000]
roman = "" # string to store the results
input = 62 # user input
for val in values[::-1]:
	#print input , "%" ,val , " = " , input % val

	results = input % val # to get the reminder
	print input , "%" , val ," =" , results

	if( results != input ):

		results = results % val
		print results
		if(val == 1000):
			roman += "M"
		elif(val == 500):
			roman += "D"
		elif(val == 100):
			roman += "C"
		elif(val == 50):
			roman += "L"
		elif(val == 10):
			roman +=  "X"
		elif(val == 5):
			roman += "V"
		elif(val == 1):
			roman += "I"
		results = results % val
		print results

print "The roman value of " , input , " is " ,roman
"""
66 % 1000  =  66
66 % 500  =  66
66 % 100  =  66
66 % 50  =  16
66 % 10  =  6
66 % 5  =  1
66 % 1  =  0
"""
