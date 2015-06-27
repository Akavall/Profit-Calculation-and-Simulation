
def calc_profit(n_periods, n_periods_before_break_up, prob_down):
    start = [1.0]
    probs_to_conv_1, probs = calc_probs(n_periods_before_break_up, prob_down, start)
    n = n_periods - n_periods_before_break_up
    probs_to_conv_2, probs = calc_probs(n, 0.5, probs)

    probs_to_conv = probs_to_conv_1 + probs_to_conv_2 

    profit_from_trading = sum(probs_to_conv)
    expected_loss = sum(i * p for i, p in zip(xrange(1, len(probs) * 2, 2), probs[1:]))
    
    return {'profit': profit_from_trading - expected_loss,
            'profit_from_trading': profit_from_trading,
            'expected_loss': expected_loss,}


def calc_probs(n_periods, prob_down, probs):
    prob_to_conv = []
    for i in xrange(n_periods):
        probs = step_one(probs, prob_down)
        probs = step_two(probs, prob_down)
        prob_to_conv.append(probs[0])
    return (prob_to_conv, probs)

def step_one(old_probs, prob_down):
    prob_up = 1.0 - prob_down
    new_probs = [0 for x in xrange(len(old_probs))]

    new_probs[0] = old_probs[0]
    if len(old_probs) > 1:
        new_probs[-1] = old_probs[-1] * prob_up

    for i in xrange(1, len(old_probs)):
        new_probs[i-1] += old_probs[i] * prob_down  
        if i < len(old_probs) - 1:
            new_probs[i] += old_probs[i] * prob_up

    return new_probs

def step_two(old_probs, prob_down):
    prob_up = 1.0 - prob_down 
    new_probs = [0 for x in xrange(len(old_probs) + 1)]
    
    new_probs[0] = old_probs[0] * prob_down
    new_probs[-1] = old_probs[-1] * prob_up

    for i in xrange(1, len(old_probs)):
        new_probs[i] += old_probs[i-1] * prob_up
        new_probs[i] += old_probs[i] * prob_down 

    return new_probs

            
        
