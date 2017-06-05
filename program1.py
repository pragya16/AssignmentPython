# Question 1: Write a python script for creating directory,displaying its contents

import os,sys
os.mkdir("dem")
os.chdir("dem")
os.system("touch a1,a2")
os.system("ls")


'''
output:
a1 a2

'''