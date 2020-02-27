import sys
import csv
import re
import string

with open("Input.txt",encoding='utf8',newline='') as obj:
   read = csv.reader(obj)
   for row in read:
      num=int(row[0])

      print("Fibonacci series for n = "+str(num)+" :")
      a = 0
      b = 1
      ser=""
      if num < 0: 
         print("Incorrect input") 
      elif num == 0:
         print(a)
      elif num == 1:
         print(a)
         print(b)
      else:
         ser+="0 1"
         for i in range(2,num): 
            c = a + b
            a = b
            b = c
            ser+=" "+str(b)
      print(ser)
