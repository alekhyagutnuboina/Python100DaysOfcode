import os
import math
from collections import  Counter

print("Sucessful push to git");

n =int(input("Enter N Value "))
ar = list(map(int,input().split()[:n]))

print(ar)


sum=0
l=[]
# for i in range(len(ar)):
#     count= ar.count(ar[i])
#     l.append(count)

for i in set(ar):
    count= ar.count(i)
    l.append(count)

c=sum(l)
print(c)


print(l)

# for x in range(len(l)):
#     if(l[x]%2  == 0 or l[x]//2 ==1):
#         sum=sum+1





#ar=[1,1,2,2,3,4,5,5,5,6,6]







# c=dict(Counter(ar))
# print(c)











