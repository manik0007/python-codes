'''Consider the following:

A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

The characters in  are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .

Input Format

The first line contains a single string denoting . 
The second line contains an integer, , denoting the length of each subsegment.

Constraints

, where  is the length of 
It is guaranteed that  is a multiple of .'''
s=input()
k=int(input())
t=int(len(s)/k)
counter=0
for i in range(0,t):
    
    ss=""
    final=""
    used=[]
    for j in range(counter,counter+k):
        ss+=s[j]
    for j in ss:
        if(j not in used):
            final+=j
        used.append(j)
    print(final)
    counter=counter+k
