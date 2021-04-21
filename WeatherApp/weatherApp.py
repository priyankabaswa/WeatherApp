# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:01:32 2020

@author: priyanka
"""
import pandas as pd

data = []
cols_n = []
data_n = []


#%% Loading data afresh

def load_data(path):
    global data_n
    global cols_n
    with open(path) as file:
        file.readline()
        df = pd.read_csv(path, sep=';', header='infer',quotechar='"', doublequote=True)
        df['Day'] = df['DateTime'].str[8:10]
        df['Month'] = df['DateTime'].str[5:7]
        df['DayMonth'] = df['Day'] + '.'
        + df['Month']
        df = df.drop(columns = ['DateTime', 'Day', 'Month'])
        #cols_n = ['DayMonth'] + [col for col in df if (col != 'DayMonth')]
        print("Loaded weather data from", path.replace(".csv", "").title())
        data_n = df.values.tolist()

#%% Loading the DATA from the csv file into a Python List
def load_data_old(path):
    global data
    with open(path) as input_file:
        input_file.readline()
        raw_data = [rows.strip().split(';') for rows in input_file]
        for rows in raw_data:
            out_date = rows[0].replace('"', '').split('-')
            data.append(
                [out_date[-1] + '.' + out_date[1], rows[1], rows[2], rows[3], (rows[4]),
                (rows[5]), (rows[6]), (rows[7]), (rows[8]), (rows[9]), (rows[10]),
                (rows[11]), (rows[12])])
    print("Loaded weather data from", path.replace(".csv", "").title())

#%% Showing the data

def show_data(display_date):
    for rows in data_n:
        if rows[0] == display_date:
            print('The weather on {} was on average {} centigrade'.format(rows[0], rows[2]))
            print('The lowest temperature was {} and the highest temperature was {}'.format(rows[3], rows[4]))
            print('There was {} mm rain'.format(rows[1]))

#%% Finding average statistics of the data
def avg_of_avg():
    global data_n
    total_mean_temp, total_min_temp, total_max_temp = 0, 0, 0
    for rows in data_n:
        total_mean_temp += float(rows[2])
        total_min_temp += float(rows[3])
        total_max_temp += float(rows[4])
    print("The average temperature for the 25 day period was", round(total_mean_temp / 25, 1))
    print("The average lowest temperature was", round(total_min_temp / 25, 1))
    print("The average highest temperature was", round(total_max_temp / 25, 1))

#%% Scatter Plot
def scatterplot():
    for rows in data_n:
        d_date = rows[0]
        temp = (round(float(rows[2])))
        print(d_date, "   " * (temp + 5) + "-")
    print("      ", end="")
    for i in range(-5, 16):
        print("{:02d} ".format(i), end="")
    print()
    
#%% Control starts from here
while True:
    print("ACME WEATHER DATA APP")
    print("1) Choose weather data file")
    print("2) See data for selected day")
    print("3) Calculate average statistics for the data")
    print("4) Print a scatterplot of the average temperatures")
    print("0) Quit program")
    x = (int(input("Choose what to do: ")))
    if x == 0:
        break
    elif x == 1:
        filename = input("Give name of the file: ")
        load_data(filename)
    elif x == 2:
        date = input("Give a date (dd.mm): ")
        show_data(date)
    elif x == 3:
        avg_of_avg()
    elif x == 4:
        scatterplot()
    else:
        print("Invalid Response")
    print()