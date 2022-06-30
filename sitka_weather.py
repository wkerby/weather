import csv
file_name = '/Users/jefferykerby/Desktop/Python/Excel Data/sitka_weather_07-2018_simple.csv'
with open(file_name) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)
    high_temp = []
    date_list = []
    for row in reader:
        high_temp.append(int(row[5]))
        date_list.append(row[2])
    print(high_temp)

for i,column_header in enumerate(header_row):
    print(str(i) + ": " + column_header + "\n")
from matplotlib import pyplot as plt
figure = plt.figure(dpi=128,figsize = (10,6))
plt.plot(date_list,high_temp, c = 'red')
plt.title("Daily high temperatures, July 2018", fontsize = 24)
plt.xlabel('',fontsize = 16)
figure.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which ='major',labelsize = 6)
plt.show()

