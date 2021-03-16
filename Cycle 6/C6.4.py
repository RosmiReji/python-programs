import csv
with open("D:\python\sample.csv", newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("Name Course")
 print("-------------")
 for row in data:
   print(row['Name'], row['Course'])
