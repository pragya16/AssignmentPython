#  Question 13: With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line

tup=(1,2,3,4,5,6,7,8,9,10)
tup1=tup[:5]
tup2=tup[5:]
print tup1
print tup2

'''
output:
[root@demo pragya_g16]# python thirteen.py
(1, 2, 3, 4, 5)
(6, 7, 8, 9, 10)

'''
