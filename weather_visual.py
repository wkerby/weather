file_name = '/Users/jefferykerby/Desktop/Python/Excel Data/sitka_weather_07-2018_simple.csv'
date_list= []
import csv
t_max_list = []
t_min_list = []
with open(file_name, 'r') as file_object:
    lines = list(csv.reader(file_object))
    for line in lines[1:]:
        date = line[2]
        date_list.append(date)
        t_max = int(line[5])
        t_max_list.append(t_max)
        t_min = int(line[6])
        t_min_list.append(t_min)

#print(date_list)
#print(t_max_list)
        
from matplotlib import pyplot as plt
figure = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(date_list, t_max_list, c = 'Red', linewidth = 3, label = "Max Temperature", alpha = 0.6)
plt.plot(date_list, t_min_list, c = 'Blue', linewidth = 3, label = "Min Temperature", alpha = 0.6)
plt.xlabel("")
#plt.ylabel("Daily Max Temperature", fontsize = 12)
plt.tick_params(axis = "both", labelsize = 5)
plt.title("Daily High Temperatures")
figure.autofmt_xdate()
plt.fill_between(date_list, t_max_list, t_min_list, facecolor = 'blue', alpha = 0.2)
plt.legend()
plt.show()


    
        
        
        
