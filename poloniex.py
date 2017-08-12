import poloniex
import time
from decimal import *
from colorama import Fore, Back, Style

# Coded By: @Uservzk80
# Github: https://github.com/uservzk80

# Thanks @dyvosvit for core of this script
# Github: https://github.com/dyvosvit

print ("Uservzk80 - Poloniex ;)")
print ("Started %s" % (time.ctime()))

def poloniexTelegram():

	class Poloniex():

		polo = poloniex.Poloniex('api-key','secret')

	class balance():


		estimatedBalance = Poloniex.polo.returnCompleteBalances()
		balance = Poloniex.polo.returnBalances()

		if balance != '':

			if estimatedBalance != 0:
				estim = 0

				for i in estimatedBalance:
					estim+=float (estimatedBalance[i]["btcValue"])

		save_balance = estim
		save_balance = Decimal(save_balance)
		file = open("balance", "w")
		file.write(str(save_balance))	
		file.close()

	class last_trades():

	    latestTrades = 30
	    save_trades = open('trades', 'w')

	    print_coins = []
	    tradeHistory24h = Poloniex.polo.returnTradeHistory('all')
	    try:
	        with open(check_coins, 'r') as afile:
	            for coin in afile:
	                print_coins += [coin.strip()]
	    except:
	        if print_coins == []:
	            print_coins = 'ETH XRP XEM LTC STR  BCN ETC DGB SC BTS DOGE DASH GNT EMC2 STEEM XMR ARDR STRAT NXT  ZEC LSK  FCT GNO NMC MAID   BURST GAME  DCR  SJCX RIC FLO REP NOTE CLAM SYS PPC EXP XVC VTC FLDC LBC AMP POT NAV XCP  BTCD  RADS   PINK GRC  NAUT  BELA  OMNI HUC NXC VRC  XPM VIA PASC  BTM NEOS XBC  BLK SBD BCY'
	            print_coins = print_coins.strip().split()
	    work_set = {}
	    for line in tradeHistory24h:
	        if line[4:] in print_coins:
	            for element in tradeHistory24h[line]:
	                signd = '-' if element['type']=='buy' else '+'
	                totald = signd+element['total']
	                thetext = 'PURCHASE: with an investment of' if element['type']=='buy' else 'SALE: with a profit of'
	                work_set[int(element['globalTradeID'])]=['BTC_'+line[4:], element['date'],element['type'].upper(), 'de',line[4:] , 'en', element['rate'],thetext,totald]
	    for key in sorted(work_set.keys(),reverse=True)[:latestTrades]:
	        colorit = Fore.RED if work_set[key][2] == 'BUY' else Fore.GREEN
	        trades = colorit+' '.join(work_set[key])
	        trades = trades[5:]
		save_trades.write(trades + ("\n\n"))

while True:

	poloniexTelegram()
	time.sleep(120)
