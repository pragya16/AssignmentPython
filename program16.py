# Question 16 : Write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24]

li = [5,6,77,45,22,12,24] 
li = [x for x in li if x%2!=0] 
print li 



'''
output:
[root@demo pragya_g16]# python sixteen.py
[5, 77, 45, 12]


'''
