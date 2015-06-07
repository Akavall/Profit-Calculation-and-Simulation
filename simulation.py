from math import factorial as fact 
import random as rn
from copy import copy
import numpy as np

# The simultion does not match theoretical results :( 

def calc_expected_n_crosses(n):
    my_sum = 0
    for k in xrange(n):
        my_sum += float(compute_combs(k)) / (2**(2*k))
    return my_sum - 1

def compute_combs(k):
    return fact(2 * k) / (fact(k) * fact(k))


# This is kinda cool, but our process is not actual random walk :(
    
def random_walk_crosses_simulation(n_turns, n_iterations):
    crosses = 0
    for _ in xrange(n_iterations):
        crosses += random_walk_crosses(n_turns)
    return crosses / float(n_iterations)

def random_walk_crosses(n):
    value = 0
    n_crosses = 0
    for _ in xrange(n):
        move = rn.gauss(0,1)
        old_value = copy(value)
        value += move 
        if (value < 0 and old_value > 0) or (value > 0 and old_value < 0):
            n_crosses += 1
    return n_crosses 

def simple_random_walk_crosses_simulation(n_turns, n_iterations):
    crosses = 0
    for _ in xrange(n_iterations):
        crosses += simple_random_walk_crosses(n_turns)
    return crosses / float(n_iterations)


def simple_random_walk_crosses(n):
    value = 0
    n_crosses = 0
    for _ in xrange(n):
        move = rn.choice((1,-1))
        value += move 
        if value == 0:
            n_crosses += 1
    return n_crosses 

# Even if conversion rate is slightly 
# above 0.5 percent (0.51) the gain
# ratio is pretty substantial 

def many_simulations(prob_down, n, n_iterations):
    sum_crosses = 0
    sum_losses = 0
    for _ in xrange(n_iterations):
        crosses_losses = one_simulation(prob_down, n)
        sum_crosses += crosses_losses[0]
        sum_losses += crosses_losses[1]
    return sum_crosses, sum_losses 

def one_simulation(prob_down, n):
    value = 0
    n_crosses = 0
    for _ in xrange(n * 2):
        if value == 0:
            value += 1
        else:
            if np.random.uniform(0,1) > prob_down:
                value += 1
            else:
                value -= 1
        if value == 0:
            n_crosses += 1
    # n_crosses is the gain that we would have 
    # value - 1 is loss that we would have
    if value == 0:
        loss = 0 
    else:
        loss = value - 1 

    return n_crosses, loss   
    





