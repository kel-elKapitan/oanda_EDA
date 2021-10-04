

import pandas as pd
import numpy as np





raw = pd.read_csv("Data_EUR_USD.csv")





def get_desc_stats(raw):



    # test for missing values

    print("The length of the list is " + str(len(raw)))



    # columns in order Time,Open,High,Low,Close,Volume,Complete

    # create distances from the raw dataset
    distances = pd.DataFrame()

    distances['o2h'] = raw['High'] - raw['Open']
    distances['o2l'] = raw['Open'] - raw['Low']
    distances['h2c'] = raw['High'] - raw['Close']
    distances['h2l'] = raw['High'] - raw['Low']
    distances['o2c'] = raw['Close'] - raw['Open']
    distances['c2l'] = raw['Close'] - raw['Low']

    print("The number or records in distances is: " + str(len(distances)))
    print(distances.head())
    print(" ")

    print("the mean of the o2h column is: " + str(distances['o2h'].mean()))
    print("the median of the o2h column is: " + str(distances['o2h'].median()))
    print("the mode of the o2h column is: " + str((distances['o2h'].max() - distances['o2h'].min())/2))
    print(" ")
    o2h_mean = distances['o2h'].mean()
    o2h_median = distances['o2h'].median()
    o2h_mode = (distances['o2h'].max() - distances['o2h'].min())/2

    print(" ")
    print(" ")


    print("the mean of the o2l column is: " + str(distances['o2l'].mean()))
    print("the median of the o2l column is: " + str(distances['o2l'].median()))
    print("the mode of the o2l column is: " + str((distances['o2l'].max() - distances['o2l'].min())/2))
    print(" ")
    o2h_mean = distances['o2l'].mean()
    o2h_median = distances['o2l'].median()
    o2h_mode = (distances['o2l'].max() - distances['o2l'].min())/2

    print(" ")
    print(" ")

    print("the mean of the h2c column is: " + str(distances['h2c'].mean()))
    print("the median of the h2c column is: " + str(distances['h2c'].median()))
    print("the mode of the h2c column is: " + str((distances['h2c'].max() - distances['h2c'].min())/2))
    print(" ")
    o2h_mean = distances['h2c'].mean()
    o2h_median = distances['h2c'].median()
    o2h_mode = (distances['h2c'].max() - distances['h2c'].min())/2

    print(" ")
    print(" ")

    print("the mean of the h2l column is: " + str(distances['h2l'].mean()))
    print("the median of the h2l column is: " + str(distances['h2l'].median()))
    print("the mode of the h2l column is: " + str((distances['h2l'].max() - distances['h2l'].min())/2))
    print(" ")
    o2h_mean = distances['h2l'].mean()
    o2h_median = distances['h2l'].median()
    o2h_mode = (distances['h2l'].max() - distances['h2l'].min())/2

    print(" ")
    print(" ")

    print("the mean of the o2c column is: " + str(distances['o2c'].mean()))
    print("the median of the o2c column is: " + str(distances['o2c'].median()))
    print("the mode of the o2c column is: " + str((distances['o2c'].max() - distances['o2c'].min())/2))
    print(" ")
    o2h_mean = distances['o2c'].mean()
    o2h_median = distances['o2c'].median()
    o2h_mode = (distances['o2c'].max() - distances['o2c'].min())/2

    print(" ")
    print(" ")

    print("the mean of the c2l column is: " + str(distances['c2l'].mean()))
    print("the median of the c2l column is: " + str(distances['c2l'].median()))
    print("the mode of the c2l column is: " + str((distances['c2l'].max() - distances['c2l'].min())/2))
    print(" ")
    o2h_mean = distances['c2l'].mean()
    o2h_median = distances['c2l'].median()
    o2h_mode = (distances['c2l'].max() - distances['c2l'].min())/2

    print(" ")
    print(" ")
    # create new variables for variance for each distance

    def variance(data):
        # Number of observations
        n = len(data)
        # Mean of the data
        mean = sum(data) / n
        # Square deviations
        deviations = [(x - mean) ** 2 for x in data]
        # Variance
        variance = sum(deviations) / n
        return variance




    var_o2h = variance(distances['o2h'])
    var_o2l = variance(distances['o2l']) 
    var_h2c = variance(distances['h2c'])
    var_h2l = variance(distances['h2l'])
    var_o2c = variance(distances['o2c'])

    print("Variance of o2h is: " + str(var_o2h))
    print("Variance of o2l is: " + str(var_o2l))
    print("Variance of h2c is: " + str(var_h2c))
    print("Variance of h2l is: " + str(var_h2l))
    print("Variance of o2c is: " + str(var_o2c))

    print(" ")
    print(" ")

    # create new variables for the standard deviation of the distances


    stdev_o2h = var_o2h ** 0.5
    stdev_o2l = var_o2l ** 0.5
    stdev_h2c = var_h2c ** 0.5
    stdev_h2l = var_h2l ** 0.5
    stdev_o2c = var_o2c ** 0.5

    print("Std Dev of o2h is: " + str(stdev_o2h))
    print("Std Dev of o2l is: " + str(stdev_o2l))
    print("Std Dev of h2c is: " + str(stdev_h2c))
    print("Std Dev of h2l is: " + str(stdev_h2l))
    print("Std Dev of o2c is: " + str(stdev_o2c))


    # add the date column from raw into distances

    distances['Date'] = raw['Time']




    # create a dataframe with 2 candles on each record, eg Time,Open1,High1,Low1,Close1,Volume1,Open2,High2,Low2,Close2,Volume2

    raw2candle = pd.DataFrame()

    raw2candle2 = pd.DataFrame()

    raw2candle = raw
    raw2candle2 = raw

    del raw2candle['Volume']
    first_df = raw2candle.drop(index=raw2candle.index[-1], axis=0, inplace=True)


    second_df = raw2candle2.drop(index=raw2candle2.index[0], axis=0, inplace=True)



    joined_raw = pd.DataFrame()

    joined_raw['Time'] = raw2candle['Time']
    joined_raw['Open1'] = raw2candle['Open']
    joined_raw['High1'] = raw2candle['High']
    joined_raw['Low1'] = raw2candle['Low']
    joined_raw['Close1'] = raw2candle['Close']

    joined_raw['Open2'] = raw2candle2['Open']
    joined_raw['High2'] = raw2candle2['High']
    joined_raw['Low2'] = raw2candle2['Low']
    joined_raw['Close2'] = raw2candle2['Close']

    # joined Raw is now ready to be used
    print("Descriptive Stats completed......")


    # return the averages, variance and std dev in tabular form for both of the datasets returned
    return distances, joined_raw




distances, joined_2_candles = get_desc_stats(raw)

print(distances)



# check distances for outliers
'''
import seaborn as sns
import matplotlib.pyplot as plt

sns.catplot(x='Sex', y='Fare', hue='Survived', 
            data=df, height=9, kind="box")



plt.xticks(rotation=90)
plt.show()
print('Done')
'''


# create a new dataframe a fill with candle formations as columns names and bool 
# records to identify wether it is a known candle formation





# long upper shadow properties
# o2h or h2c (whichever is the smaller number) / 4 (try 3.75, 3.5, 3.25, 3, 2.75 and 2.5 as alternatives)=> o2c  
# &&  
# o2c => (add c2l) or o2l(whichever is smaller) 


def is_long_upper(distances, n):

    my_mins = list()
    my_mins2 = list()
    candles_true = list()
    candles_false = list()
    AA = list()
    BB = list()

    # find the smallest of h2o and h2c
    # find the smallest of o2l and c2l, my_mins2
    for i in distances.iterrows():
        
        my_min = min(i[1][0], i[1][2])
        my_min2 = min(i[1][1], i[1][5])
        
       # divide by n
        my_min = my_min / n
        my_min2 = my_min2 / n

        my_mins.append(my_min)
        my_mins2.append(my_min2)    
    # AA. True if the above calculation if its >= o2c

    distances['my_mins'] = my_mins
    distances['my_mins2'] = my_mins2
   
    print(distances)
    print(distances.dtypes)
    for i in distances.iterrows():
        # AA is a list of the first checkpoint to test if long upper is True    
        if  i[1][7] >= i[1][4]:
            AA.append(True)
        else:
            AA.append(False)

        # BB is a list of the second checkpoint to test if long upper is True        
        # BB. True if o2c is larger than the smallest of o2l and c2l
        ######################
        ###################
        ##################
        #################

        #print(i[1][7])
       

    for i in distances.iterrows():
       
        if i[1][8] <= i[1][4]:
            BB.append(True)
        else:
            BB.append(False)
        
    print("The number of records")
    print(len(AA))
    print(len(BB))
    print('\n\n')
    print("This test is using " + str(n) + " as a divisor")




    my_bools = pd.DataFrame()
    my_bools['AA'] = AA
   
    my_bools['BB'] = BB

    print("the number of true and false values from AA and BB")
    print(my_bools.AA.value_counts())
    print(my_bools.BB.value_counts())



    # AND

    
    # create a bool list, if AA and BB are True then CC = True
    
    CC = [a and b for a, b in zip(AA, BB)]
    
    
    print(len(CC))
    # return a list or column of True/False values
    return pd.Series(CC)

    
  


# save the bool lists of whether the candle is long upper or not
is_long_upper_divide_4 = is_long_upper(distances, 4)
is_long_upper_divide_3_5 = is_long_upper(distances, 3.5)
is_long_upper_divide_3_25 = is_long_upper(distances, 3.25)
is_long_upper_divide_3 = is_long_upper(distances, 3)
is_long_upper_divide_2_75 = is_long_upper(distances, 2.75)
is_long_upper_divide_2_5 = is_long_upper(distances, 2.5)


print('variable is: 4')
print(is_long_upper_divide_4.value_counts())
print('variable is: 3.50')
print(is_long_upper_divide_3_5.value_counts())
print('variable is: 3.25')
print(is_long_upper_divide_3_25.value_counts())
print('variable is: 3')
print(is_long_upper_divide_3.value_counts())
print('variable is: 2.75')
print(is_long_upper_divide_2_75.value_counts())
print('variable is: 2.5')
print(is_long_upper_divide_2_5.value_counts())

# long lower shadow properties same as long upper but reversed



# tweezer tops Version 1

# tweezer tops Version 2

# tweezer_tops Version 3

# tweezer bottoms Version 1

# Tweezer bottoms version 2

# Tweezer bottoms Version 3


# engulfing line bearish

# engulfing line bullish

# tweezer tops Version 1














# check distances for outliers
'''
import seaborn as sns
import matplotlib.pyplot as plt

sns.catplot(x='Sex', y='Fare', hue='Survived', 
            data=df, height=9, kind="box")



plt.xticks(rotation=90)
plt.show()
print('Done')
'''