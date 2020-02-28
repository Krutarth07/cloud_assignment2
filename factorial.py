import sys
import csv
import re
import string
from datetime import datetime
import time
#import matplotlib.pyplot as plt

with open("Input.txt",encoding='utf8',newline='') as obj:
   read = csv.reader(obj)
   st=0
   ans=""
   n=[]
   t=[]
   for row in read:
      start =  time.clock()
      ans=ans+"Request ID: "+str(st)+", "
      st+=1
      timeDel=0.00003
      num=int(row[0])
      
      factorial = 1

      if num < 0:
         print("Incorrect input")
      elif num == 0:
         print("The factorial of 0 is 1")
      else:
         for i in range(1,num + 1):
             factorial = factorial*i
         msg = "The factorial of "+str(num)+" is "+ str(factorial)

      end = time.clock()
      if(st!=1 and str(num) not in n):
         n.append(str(num))
         t.append(end-start)
      ans+="Start: "+str(start)+", End: "+str(end)+", Duration: "+str((end-start))+", N: "+str(num)+"\nOutput: "+msg+"\n\n"
print(ans)

#plt.plot(n,t)
#plt.show()
