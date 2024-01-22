import csv
#import random
import time
import shutil

with open('c:/Users/t14/Downloads/sales_data.csv',newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',',quotechar='"')
    for row in reader:
        print(', '.join(row))
    data = list(reader)

source = 'c:/Users/t14/Downloads/sales_data.csv'
destination = 'c:/Users/t14/Downloads/sales_data_backup.csv'
try:
    shutil.copy(source, destination)
    print("File copied successfully")

except shutil.SameFileError:
    print("Source and destination represent the same file")


from random import shuffle
with open('c:/Users/t14/Downloads/sales_data.csv', 'r') as ip:
    data2 = ip.readlines()
    header, rest=data2[0], data2[1:]
    while True:
        time.sleep(10)
        shuffle(rest)
        with open('c:/Users/t14/Downloads/sales_data.csv', 'w') as out:
            out.write(''.join([header]+rest))