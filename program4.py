# Question4 :Write a Python program to count the number of lines in a text file

import io
fo=open("tina.txt","w+")
fo.write("hello\nTina\nGupta\nZensar")
fo.close()
filename="tina.txt"
myfile = open(filename)
lines= len(myfile.readlines())
print "There are%d lines in %s "%(lines,filename)

'''
output:
ot@demo pragya_g16]# python forth.py
There are4 lines in tina.txt
'''
