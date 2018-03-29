#!/usr/bin/env python

numbers = [ (1000,'M') ,(500,'D') , (100,'C') , (50,'L') , (10,'X') , (5,'V'), (1,'I') ] 


def roman(num):

	roman =  ""
	while num > 0:
		for i,r in numbers :
			while num >= i:
				print r
				roman += r 
				num -= 1
			return roman 

print roman(62)
