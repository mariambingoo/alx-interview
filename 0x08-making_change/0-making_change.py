#!/usr/bin/python3
#([1, 2, 25], 37))

def makeChange(coins, total):
  coins.sort() # [1 ,  2 , 25]
  sum = 0
  index = 1
  while total:

    if total < coins[-1 * index]: # 12 < 2
      index = index + 1
      if (total < 0):
        return -1
    if (total == 0):
      break
    else:
      total = total - coins[-1*index]  #12 = 12 -2
      sum = sum + 1
  return sum

print(makeChange([1, 2, 25], 37))
