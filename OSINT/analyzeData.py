import json
import requests
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import tkinter as tk


__specs__ = \
    f"""
Data Analytics,
Stock Prediction
Made by Andreas Vassilakos
    """

print(__specs__)

#get data
rsp = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=aapl&apikey=FHOXJ6KASF3JW9AR')
#rsp = requests.get('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&symbol=BTC&market=CNY&apikey=FHOXJ6KASF3JW9AR')

data = rsp.json() #create data dict.

#store data into lists for observation
dates=[]
prices=[]

for k,v in data["Weekly Time Series"].items():
    #split data into tokens
    tokens = int(k.split('-')[0])
    if tokens >2015:
        '''
        split data by date 
        idx 0  => yyyy
        idx 1  => mm
        idx 2  => dd
        '''
        dates.append(int(k.split('-')[0]))
        prices.append(float(v['1. open']))

#Convert to 1d Vector for later plottings
dates = np.reshape(dates, (len(dates), 1))
prices = np.reshape(prices, (len(prices), 1))

# Define Linear Regressor Object
regressor = LinearRegression()
regressor.fit(dates, prices)

print(len(dates))
#Predict Price on Given Date (y, m or d)
date = 2018
predicted_price =regressor.predict(date)
#display summary stats
print("Predicted price", predicted_price[0][0])
print("Confidence ( % ) of data fit", regressor.score(dates,prices))

mediancalc=np.median(prices,axis=None,out=None,overwrite_input=False,keepdims=False)
print("Median Price of all observed Prices is :", mediancalc)

highprice= np.amax(prices, axis=None, out=None, keepdims=True, initial=True)
print("Highest observed price is :", highprice)

minprice = np.amin(prices, axis=None, out=None, keepdims=True, initial=True)
print("Lowest observed price is :", minprice)

averagecalc=np.average(prices,axis=None,weights=None,returned=False)
print("Average Price of all observed Prices is :", averagecalc)

meancalc=np.mean(prices,axis=None,dtype='float64',out=None,keepdims=True)
print("Mean Price of the observed data :", meancalc)


histdes=np.histogram(prices, bins=10, range=None, normed=False, weights=None, density=None)
print("Histogram computation of the set of observed data: ",histdes)




#set simple names for graphing
x=dates
y=prices
# Visualize Results
plt.scatter(x, prices, color='indigo', label='Actual Price')  # plotting the initial datapoints
plt.plot(x, regressor.predict(x), color='crimson', linewidth=3,
         label='Predicted Price')  # plotting the line made by linear regression
plt.grid(True)
plt.ylabel('Observed Prices Range')
plt.title(' Price over Time')
plt.legend()
plt.xlabel('Date Spread')
plt.show()


# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=prices, bins='auto', color='#0504aa',alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My Very Own Histogram')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

#edw allaksa
a = np.array(histdes)
plt.hist(a, bins = [0,20,40,60,80,100])
plt.title("histogram")
plt.show()


root = tk.Tk()
root.title("Statistical Analysis")
w7 = tk.Label(root, text=("Predicted Price :", predicted_price))
w7.pack()
w = tk.Label(root, text=("Median Price of all observed Prices is :", mediancalc))
w.pack()
w2 = tk.Label(root, text=("Highest observed price is :", highprice))
w2.pack()
w3 = tk.Label(root, text=("Lowest observed price is :", minprice))
w3.pack()
w4 = tk.Label(root, text=("Average Price of all observed Prices is :", averagecalc))
w4.pack()
w5 = tk.Label(root, text=("Mean Price of the observed data :", meancalc))
w5.pack()
w6 = tk.Label(root, text=("Histogram computation of the set of observed data: ",histdes))
w6.pack()
root.wm_attributes('-alpha', 0.95)
root.mainloop()





