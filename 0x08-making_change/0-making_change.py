#!/usr/bin/python3
""" 0-making_change"""

def makeChange(coins, total):
  coins.sort() 
  sum = 0
  index = 1
  while total:

    if total < coins[-1 * index]: 
      index = index + 1
      if (total < 0):
        return -1
    if (total == 0):
      break
    else:
      total = total - coins[-1*index] 
      sum = sum + 1
  return sum