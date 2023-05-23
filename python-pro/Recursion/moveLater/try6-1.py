import numpy as np
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])

def maximumWealth(accounts):
    return max(sum(i) for i in accounts)


print(maximumWealth(twoDArray))
