def minNumberofCoinsForChange(n, denoms):
    number_of_coins = [float("inf") for _ in range(n + 1)]

    number_of_coins[0] = 0

    for item in denoms:
        for i in range(n + 1):
            if item  <= i:
                number_of_coins[i] = min(number_of_coins[i], 1 + number_of_coins[i - item])

    return number_of_coins[-1]