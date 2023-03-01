
'''import pandas as pd
data = pd.read_csv("R2_1247_3_t11_ResidentialVoltages_new.csv")
data'''
import csv



with open("R2_1247_3_t11_ResidentialVoltages_new.csv", 'r') as file:
  csvreader = csv.reader(file)
  row_count = sum(1 for row in csvreader)
  y = []
  for index, row in enumerate(csvreader):
    for x in range(9, row_count):
      if index == x:
        y.append(row[1])
        #print(row[1])

print(row_count)
