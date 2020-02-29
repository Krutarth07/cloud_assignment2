import sys
import csv
import re
import string
import time
#import matplotlib.pyplot as plt


with open("Input.txt",encoding='utf8',newline='') as obj:
   read = csv.reader(obj)
   st=0
   ans=""
   n=[]
   t=[]
   for row in read:
      start = time.clock()
      ans=ans+"Request ID: "+str(st)+", "
      st+=1
      timeDel=0.00003
      num=int(row[0])

      a = 0
      b = 1
      ser=""
      if num == 0:
         ser+=str(a)+" "
      elif num == 1:
         ser+=str(a)+" "+str(b)+" "
      else:
         ser+="0 1"
         for i in range(2,num): 
            c = a + b
            a = b
            b = c
            ser+=" "+str(b)
      end = time.clock()
      if(st!=1 and str(num) not in n):
         n.append(str(num))
         t.append(end-start)
      ans+="Start: "+str(start)+", End: "+str(end)+", Duration: "+str((end-start))+", N: "+str(num)+"\nOutput: "+ser+"\n\n"
print(ans)
#plt.plot(n,t)
#plt.show()
