# Question 6: Write a program that takes inputs from user their name and their age. And display the year in which they will turn 100 years old

import time

import datetime
Name=raw_input("Enter your Name:")

Age=int(input("Enter your Age:"))

#print '/n'Prac

print 'Hi %s ,Your present Age is %d'%(Name,Age) 
#print '/n'  
#cd=time.strftime("%d/%m/%Y") 
#cd-age 
#print cd.year

cd1=datetime.datetime.now()

cdy=cd1.year
by=int(cdy-Age)

print 'Your Bday year is %d'%by

#print '/n'

by1=int(by+100)

print 'Your age will be 100 years by 
'''
output:
[root@demo pragya_g16]# python sixthmain.py
Enter your Name:pragya
Enter your Age:24
Hi pragya ,Your present Age is 24
Your Bday year is 1993
Your age will be 100 years by 2093
'''
