# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
df = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing UCB
import random
N = 10000
d = 10
ads_selected = []
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
total_rewards = 0

for n in range(N):
    ad = 0
    max_random = 0
    for i in range(d):
        # Step - 2 from notes/ slide image in TS folder
        random_beta = random.betavariate(numbers_of_rewards_1[i]+1, numbers_of_rewards_0[i]+1)
        if (random_beta > max_random):
            max_random = random_beta
            ad = i
    # Step - 3 from notes/ slide image in UCB folder
    ads_selected.append(ad)
    reward = df.values[n, ad]
    if (reward == 1):
        numbers_of_rewards_1[ad] += 1
    else:
        numbers_of_rewards_0[ad] += 1
    total_rewards += reward

# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()