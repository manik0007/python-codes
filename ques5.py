'''You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints: 
 
The sum of the lengths of all the words do not exceed  
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, . 
The next  lines each contain a word.

Output Format

Output  lines. 
On the first line, output the number of distinct words from the input. 
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.'''

n=int(input())
a=[]
for i in range(0,n):
    s=input()
    a.append(s)
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(len(b))
ss=""
for i in b:
    ss+=str(a.count(i))
    ss+=" "
print(ss)
