import math
import numpy as np

# Setting the number of agents in the market and the amount of goods each has in their utility function
n_of_agents = 5
n_goods_per_agent = 3

a = []  # Array of 'a' values (a parameter of utility), one value per each good for each agent
r = []  # Array of ro values (a parameter of an agent's utility), one value for each agent
p = []  # Array of prices of goods
budgets = []  # Array of each the agents' budgets
c = []  # Array of c values (a variable used in equations), to be calculated from the values of 'r'

# -------------- Generating values -------------------

# Populating multi-dimensional array 'a' with random decimals in the interval [0,2) rounded to 3 decimal places
a = np.round(2 * np.random.random_sample((n_of_agents, n_goods_per_agent)), 3)

# Populating array 'r' with random decimals in the interval [-100,0) rounded to 3 decimal places
r = np.round(100 * np.random.random_sample(n_of_agents) - 100, 3)

# Generating array of prices to represent the goods
# Populating array 'p' with random decimals in the interval [5,100) rounded to 2 decimal places
p = np.round(95 * np.random.random_sample(n_goods_per_agent) + 5, 2)

# Populating array 'budgets' with random integers in the interval [25, 500)
# Using integers here is more sensible for a budget value
budgets = np.random.randint(25, 500, size=n_of_agents)

# Each sub-array in 'a' must add up to 1, recalculating all values so they satisfy this
for i in range(n_of_agents):
    curr_factor = 1 / np.sum(a[i])
    for j in range(n_goods_per_agent):
        a[i][j] = a[i][j] * curr_factor

# Populating array 'c' with calculated values ( c = p / p-1 )
# since c values are used in multiple calculations: more efficient to store these than recalculate each time
for i in range(n_of_agents):
    c.append(np.round(r[i] / (r[i] - 1),3))

# -------------- Demand calculations -------------------

# Array containing the demand calculated for all goods by all agents, size: (agents x goods)
demand = np.zeros((n_of_agents, n_goods_per_agent))  # Creating with 0 values to fix array dimensions
s = np.zeros(n_of_agents)  # Creating with 0 values to fix array dimensions

# Populating the array 's' with calculated values from the formula for S
for i in range(n_of_agents):
    for j in range(n_goods_per_agent):
        s[i] += math.pow(a[i][j], (1-c[i])) * math.pow(p[j], c[i])

print(s)

print(c)


def calcDemand(n_of_agents, n_goods_per_agent, budgets, a, c, p, s):
    demand = np.zeros((n_of_agents, n_goods_per_agent))
    for i in range(n_of_agents):
        for j in range(n_goods_per_agent):
            demand[i][j] = np.round(budgets[i] * math.pow(a[i][j], (1-c[i])) * math.pow(p[j], (c[i])-1) * math.pow(s[i], -1), 4)
    return demand

print(calcDemand(n_of_agents, n_goods_per_agent, budgets, a, c, p, s))
