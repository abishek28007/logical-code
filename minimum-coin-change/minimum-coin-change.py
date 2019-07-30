def fun(amount):
  coins = [1, 10, 25]
  numberOfCoins = [amount for i in range(0, amount+1)]
  numberOfCoins[0] = 0
  for i in range(1,amount+1):
    for j in range(0,len(coins)):
      numberOfCoins[i] = numberOfCoins[i] if numberOfCoins[i] < numberOfCoins[i - coins[j]]+1 else numberOfCoins[i - coins[j]]+1
  print(numberOfCoins[amount])

fun(31)
