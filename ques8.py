'''There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

Input Format

The first line contains a single integer , the number of test cases. 
For each test case, there are  lines. 
The first line of each test case contains , the number of cubes. 
The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

Constraints 
 
 

Output Format

For each test case, output a single line containing either "Yes" or "No" without the quotes.'''

t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    t=input()
    a = list(t.split(" "))
    flag=0
    if(int(a[0])>int(a[-1])):
        last=int(a[0])
    else:
        last=int(a[-1])
    while(len(a)>0):
        if(last<int(a[0]) or last<int(a[-1])):
            flag=1
            break
        if(int(a[0])>int(a[-1])):
            last=int(a[0])
            a.pop(0)
            
        else:
            last=int(a[-1])
            a.pop()
    if (flag==0):
        print("Yes")
    else:
        print("No")
        flag=0
