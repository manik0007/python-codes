'''A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

 would have it's logo with the letters .'''
s=input()
l=[]
for i in range(26):
    l.append(0)
for i in s:
    l[ord(i)-ord('a')]+=1

m=0
for i in range(len(l)):
    if l[i]>l[m]:
        m=i
print(chr(m+ord('a'))+" "+str(l[m]))
l[m]=0

m=0
for i in range(len(l)):
    if l[i]>l[m]:
        m=i
print(chr(m+ord('a'))+" "+str(l[m]))
l[m]=0

m=0
for i in range(len(l)):
    if l[i]>l[m]:
        m=i
print(chr(m+ord('a'))+" "+str(l[m]))
l[m]=0
