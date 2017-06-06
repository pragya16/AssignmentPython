#  Question 8: Define a function max() that takes two numbers as arguments and returns the largest of them


def largeValue(a,b):
        if a>b:
                print(str(a) + "is larger then " + str(b))
        else:
                print(str(b) + " is larger then " + str(a))
print ("enter the first number:")
aA=input()
print("enter the second number")
bB=input()
largeValue(aA,bB)

'''
output:
[root@demo pragya_g16]# python eighth.py
enter the first number:
23
enter the second number
45
45 is larger then 23

'''
