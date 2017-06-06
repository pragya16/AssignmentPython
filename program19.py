# Question 19:Write a function find_longest_word() that takes a list of words and returns the length of the longest one

text = "I love professional yodeling more than college football and I love you Astha sooooooooooooooo much" 
longest = 0
for word in text.split():   
 if len(word) > longest:        
    longest = len(word)        
    longest_word = word
print( "The longest word is %s" % longest_word )

'''
output:
[root@demo pragya_g16]# python ninteen.py
The longest word is sooooooooooooooo

'''
