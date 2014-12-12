combos = 0

def coins(rest, coin):
	global combos

	if rest == 0:
		combos += 1
		return

	if coin == 0: value = 200
	elif coin == 1: value = 100
	elif coin == 2: value = 50
	elif coin == 3: value = 20
	elif coin == 4: value = 10
	elif coin == 5: value = 5
	elif coin == 6: value = 2
	elif coin == 7: value = 1
	else: return

	while rest >= 0:
		coins(rest, coin + 1)
		rest -= value

coins(200,0)
print(combos)
