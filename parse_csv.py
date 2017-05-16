import csv
import re

file='responses.csv'

with open(file, 'rb') as csvfile:
     filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
     next(filereader, None)
     data=range(0)
     for row in filereader:
         #print row[1:5]
         m1 = re.search('([0-9][0-9])|([0-9])', row[1])
         m2 = re.search('([0-9][0-9])|([0-9])', row[2])
         m3 = re.search('([0-9][0-9])|([0-9])', row[3])
         m4 = re.search('([0-9][0-9])|([0-9])', row[4])
         m5 = re.search('([0-9][0-9])|([0-9])', row[5])
         lm=[int(m1.group(0)),int(m2.group(0)),int(m3.group(0)),int(m4.group(0)),int(m5.group(0))]

         data.append(lm)
print data

