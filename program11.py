
# Question 11:Write a program that accepts a sentence and calculate the number of letters and digits.
            #  Suppose the following input is supplied to the program:
             # i/p: Hello Priya 1287
             # o/p: LETTERS 10
                   #  DIGITS 4


str=raw_input("enter string") 
d=l=0
for c in str:        
	if c.isdigit():                
		d=d+1        
	elif c.isalpha():                
		l=l+1        
	else:                
		pass
print("letters",l)
print("digits",d)


'''
output:
[root@demo pragya_g16]# python eleven,py
enter string pragya
('letters', 6)
('digits', 0)

'''
