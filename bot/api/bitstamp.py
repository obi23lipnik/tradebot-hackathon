from urllib import request
from json import loads
import requests
import hmac
import hashlib
import time

from ... tradebot import config

def nonce():
	return str(int(time.time()*1000))

def signature():
	API_SECRET=config.bitstamp.SECRET
	message = "{}{}{}".format(nonce(),config.bitstamp.USER_ID,config.bitstamp.API_KEY)
	return hmac.new(
        API_SECRET.encode('utf8'),
        msg=message.encode('utf8'),
        digestmod=hashlib.sha256
		).hexdigest().upper()

class responder:
	def str_response(response):
		return response.readall().decode('utf-8')

	def getTicker(type):
		response = request.urlopen("https://www.bitstamp.net/api/v2/ticker/"+type+"/")
		return response.text

	def getHourlyTicker(type):
		response = request.urlopen("https://www.bitstamp.net/api/v2/ticker_hour/"+type+"/")
		return response.text

	def getOrderBook(type):
		response = request.urlopen("https://www.bitstamp.net/api/v2/order_book/"+type+"/")
		return response.text

	def getTransactions(type, **kwargs):
		if 'time' in kwargs:
			response = request.urlopen("https://www.bitstamp.net/api/v2/transactions/"+type+"/",params={ "time" : kwargs["time"]})
		else:
			response = request.urlopen("https://www.bitstamp.net/api/v2/transactions/"+type+"/")
		return response.text

	def getConversion(type):
		response = request.urlopen("https://www.bitstamp.net/api/"+type+"/")
		return response.text

	def getAccBalance(self):
		response = requests.post("https://www.bitstamp.net/api/v2/balance/",
			data={
				"key": config.bitstamp.API_KEY,
				"nonce": nonce(),
				"signature": signature(),
	    })
		return response.text

	def userTransactions(self):
		response = requests.post("https://www.bitstamp.net/api/v2/user_transactions/",
			data={
				"key": config.bitstamp.API_KEY,
				"nonce": nonce(),
				"signature": signature(),
	    })
	
		return response.text

	def buyLimitOrder(amount, price, type):
		response = requests.post("https://www.bitstamp.net/api/v2/buy/"+type+"/",
			data={
				"key": config.bitstamp.API_KEY,
				"nonce": nonce(),
				"signature": signature(),
				"amount": amount,
				"price": price,
	    })
		return response.text

	def sellLimitOrder(amount, price, type):
		response = requests.post("https://www.bitstamp.net/api/v2/sell/"+type+"/",
			data={
				"key": config.bitstamp.API_KEY,
				"nonce": nonce(),
				"signature": signature(),
				"amount": amount,
				"price": price,
	    })
		return response.text