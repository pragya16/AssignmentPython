# Question 9: Define a function max_of_three() that takes three numbers as arguments and returns the largest of them

def Largest(a,b,c):
        max = a        
	if(b> max)and (b>c):                
		max = b        
	elif (c > max):                
		max=c        
	return max
print Largest(1,6,13)

'''
output:
[root@demo pragya_g16]# python nine.py
13

'''
