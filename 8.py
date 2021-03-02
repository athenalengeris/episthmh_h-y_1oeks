import os
import requests
import cryptocompare

CRYPTOCOMPARE_KEY = os.environ.get('CRYPTOCOMPARE_KEY', '838fc5b7d2399f78d16c2a4126f0cd1e6a28bbfe88c5e82b0c8bf7213bd507a2')

btc1 = cryptocompare.get_price('BTC')
ltc1 = cryptocompare.get_price('LTC')
eth1 = cryptocompare.get_price('ETH')

btc2=btc1['BTC']
ltc2=ltc1['LTC']
eth2=eth1['ETH']

btc_price=btc2['EUR']
ltc_price=ltc2['EUR']
eth_price=eth2['EUR']


f = open('crypto.txt')

btc_num = 1.345
ltc_num = 8.2
eth_num = 1.234


summ=btc_price*btc_num + ltc_price*ltc_num + eth_price*eth_num

print('Έχει '+ str(summ) + '  ευρώ συνολικά.')

f.close()
