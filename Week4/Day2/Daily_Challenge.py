num_of_candles = random.randint(0,9)
print(num_of_candles)
if num_of_candles % 2 == 0:
    half_of_candles = num_of_candles//2
    candle_string = 'i' * half_of_candles + "_" + 'i' * half_of_candles
else:
    candle_string = 'i' * num_of_candles
print(candle_string)
num_of_spaces = 11 - len(candle_string)
candle_string += '_' * (num_of_spaces//2)
candle_string  =  '_' * (num_of_spaces//2) + candle_string
print(candle_string)
cake = f'''
       {candle_string}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
'''
print(cake)
