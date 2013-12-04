#!/usr/bin/python

import urllib
import json
import time

class btc_e():
	
	def __init__(self):
		self.update_time = 0
		pass
	
	def update(self):
		data = urllib.urlopen("https://btc-e.com/api/2/ltc_btc/ticker").read()
		data = json.loads(data)
		data = data["ticker"]

		self.buy_ = data["buy"]
		self.sell_ = data["sell"]

		self.update_time = time.time()

	def buy(self):

		if time.time() - self.update_time > 10:
			self.update()

		return(self.buy_)
	def sell(self):
		if time.time() - self.update_time > 10:
			self.update()
		
		return(self.sell_)

class bit_finex():
	
	def __init__(self):
		self.update_time = 0
		pass

	def update(self):
		data = urllib.urlopen("https://api.bitfinex.com/v1/ticker/ltcbtc").read()
		data = json.loads(data)

		self.buy_ = float(data["last_price"])
		self.sell_ = float(data["last_price"])

		self.update_time = time.time()

	def buy(self):
		if time.time() - self.update_time > 10:
			self.update()
		return(self.buy_)
	def sell(self):
		if time.time() - self.update_time > 10:
			self.update()	
		return(self.sell_)

class crypto_trade():

	def __init__(self):
		self.update_time = 0
		pass
	
	def update(self):
		data = urllib.urlopen("https://www.crypto-trade.com/api/1/ticker/ltc_btc").read()
		data = json.loads(data)
		data = data["data"]

		self.buy_ = float(data["max_bid"])
		self.sell_ = float(data["min_ask"])
	
		self.update_time = time.time()

	def buy(self):
		if time.time() - self.update_time > 10:
			self.update()
		return(self.buy_)
	def sell(self):
		if time.time() - self.update_time > 10:
			self.update()
		return(self.sell_)

class vir_curex():

	def __init__(self):
		self.update_time = 0
		pass
	
	def update(self):
		data = urllib.urlopen("https://vircurex.com/api/get_highest_bid.json?base=LTC&alt=BTC").read()
		data = json.loads(data)
		self.buy_ = float(data["value"])
		
		data = urllib.urlopen("https://vircurex.com/api/get_lowest_ask.json?base=LTC&alt=BTC").read()
		data = json.loads(data)
		self.sell_ = float(data["value"])

		self.update_time = time.time()

	def buy(self):
		if time.time() - self.update_time > 10:
			self.update()
		return(self.buy_)
	def sell(self):
		if time.time() - self.update_time > 10:
			self.update()
		return(self.sell_)

btce = btc_e()
bitfinex = bit_finex()
cryptotrade = crypto_trade()
#vircurex = vir_curex()


def tick():
	log = open("ltc.log","a")
	log.write("%s |" % (int(time.time())),) #less jittery output
	log.write("BTC-E: %.4f/%.4f |" % (btce.buy(),btce.sell()),)
	log.write("BitFinex: %.4f/%.4f |" % (bitfinex.buy(),bitfinex.sell()),)
	log.write("CryptoTrader: %.4f/%.4f |" % (cryptotrade.buy(),cryptotrade.sell()),)
#	print "VirCurex %s/%s" % (vircurex.buy(),vircurex.sell()),
	log.write("\n")
	log.close()

if __name__ == "__main__":

	while True:
		tick()
		time.sleep(10)
	
