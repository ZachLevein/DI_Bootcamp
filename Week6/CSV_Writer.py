import csv 

file = open('test.csv', 'a', newline = '')

tup1 = ('zach', '22')

writer = csv.writer(file)

writer.writerow(tup1)

file.close()
