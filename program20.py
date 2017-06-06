# Question 20: Ask the user for a string and print out whether this string is a palindrome or not


word= 'madam'
word_rev = reversed(word)
def is_palindrome(word):
        if list(word) ==  list(word_rev):
                 print'True, it is a palindrome'
        else:
                 print'False, this is''t a plindrome'
is_palindrome(word)



'''
output:
[root@demo pragya_g16]# python palindrom.py
True, it is a palindrome
'''

