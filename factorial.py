import sys
import csv
import re
import string

with open("Input.txt",encoding='utf8',newline='') as obj:
   read = csv.reader(obj)
   st=0
   for row in read:
      num=int(row[0])
      
      factorial = 1

      if num < 0:
         print("Incorrect input")
      elif num == 0:
         print("The factorial of 0 is 1")
      else:
         for i in range(1,num + 1):
             factorial = factorial*i
         print("The factorial of",num,"is",factorial)
