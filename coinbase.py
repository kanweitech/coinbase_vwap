import websocket
import json
import dateutil.parser
import numpy as np

minutes_processed = {}
minute_candlesticks = []
volume = []
current_tick = None
previous_tick = None



def on_open(ws):
	print("opened connection")

	subscribe_message = {
		"type": "subscribe",
		"channels": [
			{
				"name": "ticker",
				"product_ids": [
					"BTC-USD",
				]
			}
		]
	}

	ws.send(json.dumps(subscribe_message))

def on_message(ws, message):
	global current_tick, previous_tick

	previous_tick = current_tick
	current_tick = json.loads(message)



	print("=== Received Tick ===")
	print("{} @ {} => {}, ===> volume_24h:{}".format(current_tick['time'], current_tick['price'], price, current_tick['volume_24h']))


	tick_datetime_object = dateutil.parser.parse[current_tick['time']]
	tick_dt = tick_datetime_object.strftime("%m/%d/%Y %H:%M")
	print(tick_datetime_object.minute)
	print(tick_dt)

	

	# vwap = np.sum(np.multiply(current_tick['price'], current_tick['volume_24h']))/np.sum(current_tick['volume_24h'])
	




socket = "wss://ws-feed.exchange.coinbase.com"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)

ws.run_forever()



















	# if not tick_dt in minutes_processed:
	# 	print("starting new candlestick")
	# 	minutes_processed[tick_dt] = True
	# 	print(minutes_processed)

	# 	minute_candlesticks.append({
	# 		"minute": tick_dt,
	# 		"open": current_tick['price'],
	# 		"high": current_tick['price'],
	# 		"low": current_tick['price']
	# 		})
	# if len(minute_candlesticks) > 0:
	# 	current_candlestick = minute_candlesticks[-1]
	# 	if current_tick['price'] > current_candlestick['high']:
	# 		current_candlestick['high'] = current_tick['price']
	# 	if current_tick['price'] < current_candlestick['low']:
	# 		current_candlestick['low'] = current_tick['price']

	# 	print("=== Candlesticks ===")
	# 	for candlestick in minute_candlesticks:
	# 		print(candlestick)
	





# {
# 	'type': 'ticker', 
# 	'sequence': 31164690831, 
# 	'product_id': 'BTC-USD', 
# 	'price': '59001', 
# 	'open_24h': '60196.21', 
# 	'volume_24h': '21606.07415090', 
# 	'low_24h': '58558', 
# 	'high_24h': '61418.19', 
# 	'volume_30d': '388259.67333583', 
# 	'best_bid': '59000.99', 
# 	'best_ask': '59001.00', 
# 	'side': 'buy', 
# 	'time': '2021-11-17T10:31:20.504070Z', 
# 	'trade_id': 237394051, 
# 	'last_size': '0.00016931'
# }