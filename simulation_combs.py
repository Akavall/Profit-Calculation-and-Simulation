import numpy as np 
from math import factorial as fact

def calc_loss_combinations(n, prob_down):
    total_loss = 0
    prob_up = 1.0 - prob_down
    total_probs = 0

    for i in xrange(1, n+1):
        combs = fact(n * 2) / (fact(n+i) * fact(n-i))
        prob = prob_up ** (n+i) * prob_down ** (n-i)
        single_loss = (i*2) * combs * (prob * 2)
        total_loss += single_loss
        print "combs: {}".format(combs)
        if i > 0:
            total_probs += (prob * 2 * combs)
        else:
            total_probs += (prob * combs)
    return total_loss, total_probs 

def many_simulations(n, prob_down, n_simulations):
    sum_loss = 0
    for i in xrange(n_simulations):
        sum_loss += one_round(n, prob_down)
    return float(sum_loss) / n_simulations

def one_round(n, prob_down):
    start = 0
    for i in xrange(n * 2):
        if np.random.uniform(0, 1) > prob_down:
            start += 1
        else:
            start -= 1
    if start > 0:
        start = (start - 1) * 2
    else:
        start = 0
    return start 
