import numpy as np
import matplotlib.pyplot as plt 
import logging 
import pandas as pd 

logging.getLogger().setLevel(logging.INFO)

def one_pairs_gen(n_periods, conv_rate, break_up_prob_period, variance):
    true_value = [100]
    x = [100]
    y = [100]
    # break_up_prob_period = calc_break_up_prob_period(n_periods, break_up_prob_run)

    break_up = False 
    # We need to modify break up prob, such that probability
    # we are talking about probility to break up during 
    # the the whole run, not 1 period 
    for i in xrange(n_periods):
        if not break_up and np.random.uniform(0, 1) < break_up_prob_period:
            break_up = True 

        delta = np.random.uniform(-variance, variance)
        true_value.append(true_value[-1] + delta)

        delta_x = np.random.uniform(-variance, variance)
        delta_y = np.random.uniform(-variance, variance)

        if not break_up:                                    
            if x[-1] < true_value[-1]:
                delta_x += ((true_value[-1] - x[-1]) * conv_rate)
            else:
                delta_x -= ((x[-1] - true_value[-1]) * conv_rate)

            if y[-1] < true_value[-1]:
                delta_y += ((true_value[-1] - y[-1]) * conv_rate)
            else:
                delta_y -= ((y[-1] - true_value[-1]) * conv_rate)

        x.append(x[-1] + delta_x)
        y.append(y[-1] + delta_y)

    result = {'true_value': true_value, 'x': x, 'y': y}
    return result 

def calc_profit_sim_wrapper(n_periods, conv_rate, break_up_prob_period, variance, thresh, n_iterations):
    profit = 0
    profit_from_trading = 0
    loss = 0
    number_of_transactions = 0
    trade_info = {}
    for _ in range(n_iterations):
        price_paths = one_pairs_gen(n_periods, conv_rate, break_up_prob_period, variance)
        trade_result = calc_profit(price_paths['x'], price_paths['y'], thresh)

        profit += trade_result['profit']
        profit_from_trading += trade_result['profit_from_trading']
        loss += trade_result['loss']
        number_of_transactions += trade_result['number_of_transactions']

    trade_info = {}
    trade_info['profit'] = profit / n_iterations
    trade_info['profit_from_trading'] = profit_from_trading / n_iterations
    trade_info['loss'] = loss / n_iterations
    trade_info['number_of_transactions'] = float(number_of_transactions) / n_iterations

    return trade_info
    
def calc_profit(x, y, thresh):
    profit_from_trading = 0
    bought_x = False
    bought_y = False 
    bought_gap = 0
    number_of_transactions = 0

    for ele_x, ele_y in zip(x, y):

        if not bought_x and not bought_y:
            if ele_x - ele_y > thresh:
                bought_gap = ele_x - ele_y
                bought_y = True
                number_of_transactions += 1
            elif ele_y - ele_x > thresh:
                bought_gap = ele_y - ele_x 
                bought_x = True
                number_of_transactions += 1
        else:
            if bought_x:
                if ele_x >= ele_y:
                    profit_from_trading += (bought_gap + ele_x - ele_y)
                    bought_x = False
            elif bought_y:
                if ele_y >= ele_x:
                    profit_from_trading += (bought_gap + ele_y - ele_x)
                    bought_y = False 

    if bought_x:
        loss = (ele_y - ele_x) - bought_gap
        
    elif bought_y:
        loss = (ele_x - ele_y) - bought_gap
        
    else:
        loss = 0

    return {'profit': profit_from_trading - loss,
            'profit_from_trading': profit_from_trading,
            'loss': loss,
            'number_of_transactions': number_of_transactions}


def show_plot(result_dict):
    df = pd.DataFrame(result_dict)
    df.plot()
    plt.show()

# def calc_break_up_prob_period(n_periods, break_up_prob_run):
#     return (break_up_prob_run + 1) ** (1.0 / n_periods) - 1

    
    
        
