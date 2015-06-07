import numpy as np


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
    





