# Question 17: With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists



def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) &  set(b))


if __name__ == "__main__": 
    a = [1,3,6,78,35,55]
    b = [12,24,35,24,88,120,155]
    print intersect(a, b)

'''
output:
[root@demo pragya_g16]# python seventeen.py[35]

'''

