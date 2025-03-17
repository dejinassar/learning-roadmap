x = 2
try:
  print(x / 0)
except NameError:
  print('NameError means sometin is undefined')
except ZeroDivisionError:
  print('Please do not divide by zero.')