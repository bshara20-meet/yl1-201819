#a=[1,2,45,6]
#print(a[0])
#print(a[-1])

#a=[2,4,6,8,10,12,14]
#for num in a:
#	if num < 5:
#		print(num)
#f=[]
#a = [1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#for i in b:
#	for c in a:
#		if i==c:
#			if i not in f:
#				f.append(i)
#
#print(f)
#
import tkiner as tk
from tkiner import simpledialog
num=4
for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
    	print(num,"is a prime number")