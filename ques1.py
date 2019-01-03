'''Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
'''
str = input()
substring = []
allstring=[]
vowels="AEIOU"
stuart=0
kevin=0
count=0
for counter in range (0,len(str)):
    for j in range(0,len(str)):
        if(counter<len(str)-j):
            if(str[counter:len(str)-j] not in substring):
                substring.append(str[counter:len(str)-j])
            allstring.append(str[counter:len(str)-j])
for i in substring:
    for j in range(0,len(allstring)):
        if(i==allstring[j]):
            count+=1
    for first in i:
        if first in vowels:
            kevin+=count
        else:
            stuart+=count
        break
    count=0
if(kevin>stuart):
    print("Kevin ",kevin)
if(stuart>kevin):
    print("Stuart ",stuart)
if(kevin==stuart):
    print("Draw")
