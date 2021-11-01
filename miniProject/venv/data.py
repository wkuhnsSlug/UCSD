import json
import numpy as np
import urllib.request
import requests


APIKEY=""
url="https://www.quandl.com/api/v3/datasets/FSE/AFX_X.json?start_date=2017-01-01&end_date=2017-12-31&api_key="+APIKEY
jsonOutput=requests.get(url).json()
dataset= jsonOutput['dataset']['data']

stock_date  = [elem[0] for elem in dataset if elem[0] != None]
stock_open  = [elem[1] for elem in dataset if elem[1] != None]
stock_high  = [elem[2] for elem in dataset if elem[2] != None]
stock_low   = [elem[3] for elem in dataset if elem[3] != None]
stock_close = [elem[4] for elem in dataset if elem[4] != None]
stock_vol   = [elem[6] for elem in dataset if elem[6] != None]
stock_turn  = [elem[7] for elem in dataset if elem[7] != None]

def get_max_val(array):
    '''
    :param float or int array:
    :return: int
    '''
    max_val = array[0]
    for num in array:
        if num > max_val:
            max_val = num
    return max_val

def get_min_val(array):
    '''
    :param array:float or int
    :return: int
    '''
    min_val = array[0]
    for num in array:
        if num < min_val:
            min_val = num
    return min_val

def largest_change_one_day(s_low, s_high):
    '''
    :param s_low: float or int
    :param s_high: float or int
    :return: float or int
    '''
    delta = [high - low for low, high in zip(s_low, s_high)]
    max_delta = get_max_val(delta)
    return max_delta

def largest_delta_two_days_close(s_close):
    '''
    :param s_close: float or int
    :return: float or int
    '''
    delta_2d = [abs(s_close[i + 1] - s_close[i]) for i in range(len(s_close) - 1)]
    max_delta_2days = get_max_val(delta_2d)
    return max_delta_2days

def avg_daily_vol(s_vol):
    '''
    :param s_vol: float or int
    :return: float or int
    '''
    total_vol = 0
    for vol in s_vol:
        total_vol = total_vol + vol
    avg_vol = total_vol / len(s_vol)
    return (avg_vol)

def get_median(array):
    '''
    :param array: float or int
    :return:float or int
    '''
    array.sort()
    med_index = len(array) // 2
    median = (array[med_index] + array[~med_index]) / 2
    return (median)

min_open = get_min_val(stock_open)
max_open = get_max_val(stock_open)
max_change = largest_change_one_day(stock_low,stock_high)
max_change_two_days = largest_delta_two_days_close(stock_close)
avg_daily_vol_2017 = avg_daily_vol(stock_vol)
median_volume_2017 = get_median(stock_vol)

print('3a. The lowest  Opening Price: ${:0.2f}'.format(min_open))
print('3b. The highest Opening Price: ${:0.2f}'.format(max_open))
print('4. The largest change in one day : ${:0.2f}'.format(max_change))
print('5. The largest change in any two days (based on close price): ${:0.2f}'.format(max_change_two_days))
print('6. Average daily trading volume during this year: {:0,.2f} units'.format(avg_daily_vol_2017))
print('6. Median trading volume during this year: {:0,.2f} units'.format(median_volume_2017))