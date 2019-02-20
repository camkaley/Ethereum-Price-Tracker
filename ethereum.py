# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:41:13 2017

@author: camka
"""

from urllib.request import urlopen
import json
import time
import os
a = 0
myeth = 10.5
moneypaid = 5200
moneypaidusd = 4077.32

data = open("ethereum.txt", "r")
datalines = data.readlines()
firstprice = datalines[0]
oldprice = datalines[len(datalines) - 1]
data.close()
firstprice = firstprice.split(":")[0]
oldprice = oldprice.split(":")[0]
pricearray = []
datearray = []

while 1 == 1:
	try:
	    response = urlopen('https://api.coinbase.com/v2/exchange-rates')
	    html = response.read()
	    
	    parsed_json = json.loads(html)
	    
	    oneusd = parsed_json['data']['rates']['ETH']
	    oneaud = parsed_json['data']['rates']['AUD']
	    ethusd = 1 / float(oneusd)
	    audeth = ethusd * float(oneaud)
	    
	    if (a == 0):
	        data = open("ethereum.txt", "a")
	        data.write(str(audeth) + ":" + time.strftime("%d/%m/%Y") + "\n")
	        data.close();
	        a = 1

	    for line in datalines:
		    line = line.split(":")
		    price = line[0]
		    date = line[1]
		    date = date.replace("/", "")
		    pricearray.append(price)
		    datearray.append(date)    
	    change = round(((audeth / float(oldprice)) * 100 - 100), 2)
	    totalchange = round(((audeth / float(firstprice)) * 100 - 100), 2)
	    profitaud = (myeth * audeth) - moneypaid
	    profitusd = (myeth * ethusd) - moneypaidusd
	    
	    print("Ethereum Price AUD: $" + str(round((audeth), 2 )))
	    print("Ethereum Price USD: $" + str(round((ethusd), 2 )))
	    print("Percent Changed Since Last Round: " + str(change) + "%") 
	    print("Percent Changed Overall: " + str(totalchange) + "%") 
	    print("Profit: ~ $" + str(round((profitaud), 2 )) + " AUD / $" + str(round((profitusd), 2 )) + " USD")
	    time.sleep(60)
	    os.system('cls')

	except:
		print("Error connection to API, retrying in 3 seconds...")
		time.sleep(3)
