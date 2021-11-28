import numpy as np
import math

n_of_agents = 5
n_goods_per_agent = 3

a = [[0, 0.1, 0.2], [0.3, 0.4, 0.5], [0.6, 0.7, 0.8], [1, 1.2, 1.5], [1.65, 1.855, 1.9]]
r = [-100.0, -75.5, -40.111, -5, -0.5]
p = [5, 35.55, 70]
budgets = [25, 100, 240, 371, 499]
c = []

for i in range(n_of_agents):
    curr_factor = 1 / np.sum(a[i])
    for j in range(n_goods_per_agent):
        a[i][j] = a[i][j] * curr_factor

for i in range(n_of_agents):
    c.append(np.round(r[i] / (r[i] - 1), 3))


s = np.zeros(n_of_agents)

for i in range(n_of_agents):
    for j in range(n_goods_per_agent):
        s[i] += math.pow(a[i][j], (1 - c[i])) * math.pow(p[j], c[i])


def calcDemand(n_of_agents, n_goods_per_agent, budgets, a, c, p, s):
    demand = np.zeros((n_of_agents, n_goods_per_agent))
    for i in range(n_of_agents):
        for j in range(n_goods_per_agent):
            demand[i][j] = np.round(budgets[i] * math.pow(a[i][j], (1-c[i])) * math.pow(p[j], (c[i])-1) * math.pow(s[i], -1), 4)
    return demand

# --------- Tests -----------

# Testing a[1] after reformatting here: all the values of this subarray must add up to 1
if((a[1][0] + a[1][1] + a[1][2]) == 1):
    print("Test for 'a' has passed.")
else: print("Test for 'a' has failed.")

# Testing c[1]: must be equal to -75.5 / (-75.5 - 1) = 0.987 (rounded to 3 dec)
if(c[1] == 0.987):
    print("Test for 'c' has passed.")
else: print("Test for 'c' has failed.")

# Testing s[1]: from manually calculating from the equation for s, must be equal to 103.7543 (rounded to 4 dec)
if((np.round(s[1], 4)) == 103.7543):
    print("Test for 's' has passed.")
else: print("Test for 's' has failed.")

# Testing the demand function for a[1] and good p[0] (agent #2 and good #1)
# By manual calculations, must be equal to 0.9270018107 rounded to 4 dec
if(calcDemand(n_of_agents, n_goods_per_agent, budgets, a, c, p, s)[1][0] == 0.927):
    print("Test for 'calcDemand' function has passed.")
else: print("Test for 'calcDemand' function has failed.")
