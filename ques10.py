'''You are given a string . 
 contains alphanumeric characters only. 
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .'''

s=input()
lower=[]
upper=[]
even=[]
odd=[]
final=""
for i in s:
    n=ord(i)
    if(n>=65 and n<=90):
        upper.append(i)
    if(n>=97 and n<=122):
        lower.append(i)
    if(n>=48 and n<=57):
        if(int(i)%2==0):
            even.append(i)
        else:
            odd.append(i)
lower.sort()
upper.sort()
even.sort()
odd.sort()
for i in lower:
    final+=i
for i in upper:
    final+=i
for i in odd:
    final+=str(i)
for i in even:
    final+=str(i)
print(final)
