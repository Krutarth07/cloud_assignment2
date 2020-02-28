import random
import csv

fall= open('Input.txt', 'w', encoding="utf-8",newline='')
wrall = csv.writer(fall)

for i in range(0,20):
    l=[]
    l.append(random.randint(0,9))
    wrall.writerow(l)

