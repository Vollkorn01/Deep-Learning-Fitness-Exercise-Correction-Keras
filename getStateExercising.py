import csv
import re

with open('./Dataset/Test/19-05-13_13-37-02/squat1.txt', 'r') as in_file:
   stripped = (line.strip() for line in in_file)
   noTabs = (line.replace("    ", "") for line in stripped)
   lines = (line.split(";") for line in noTabs if re.match("(.*)STATE_(EXER|DONE)(.*)", line))
   for line in lines:
    print(line)
   with open('./Dataset/Test/19-05-13_13-37-02/squat1_exercising.csv', 'w') as out_file:
       writer = csv.writer(out_file)
       writer.writerows(lines)