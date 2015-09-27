import numpy as np
import matplotlib.pyplot as plt 
import logging 
import pandas as pd 

logging.getLogger().setLevel(logging.INFO)

def one_pairs_gen(n_periods, conv_rate, break_up_prob, variance):
    true_value = [100]
    x = [100]
    y = [100]
    break_up = False 
    for i in xrange(n_periods):
        if not break_up and np.random.uniform(0, 1) < break_up_prob:
            break_up = True 
            # logging.info("Broke up on: {}".format(i))

        delta = np.random.uniform(-variance, variance)
        true_value.append(true_value[-1] * (1 + delta))

        delta_x = np.random.uniform(-variance, variance)
        delta_y = np.random.uniform(-variance, variance)

        if not break_up:                                    
            if x[-1] < true_value[-1]:
                delta_x += (np.random.uniform(0, variance) * conv_rate)
            else:
                delta_x -= (np.random.uniform(0, variance) * conv_rate)

            if y[-1] < true_value[-1]:
                delta_y += (np.random.uniform(0, variance) * conv_rate)
            else:
                delta_y -= (np.random.uniform(0, variance) * conv_rate)

        x.append(x[-1] * (1 + delta_x))
        y.append(y[-1] * (1 + delta_y))

    return {'true_value': true_value, 'x': x, 'y': y}

def calc_profit_sim_wrapper(n_periods, conv_rate, break_up_prob, variance, thresh, n_iterations):
    total_profits = 0
    for _ in range(n_iterations):
        price_paths = one_pairs_gen(n_periods, conv_rate, break_up_prob, variance)
        total_profits += calc_profit(price_paths['x'], price_paths['y'], thresh)['profit']

    return total_profits / n_iterations
    

def calc_profit(x, y, thresh):
    profit_from_trading = 0
    bought_x = False
    bought_y = False 
    for ele_x, ele_y in zip(x, y):
        if not bought_x and not bought_y:
            if ele_x - ele_y > thresh:
                bought_y = True
            elif ele_y - ele_x > thresh:
                bought_x = True
        else:
            if bought_x:
                if ele_x > ele_y:
                    profit_from_trading += thresh
                    bought_x = False
            elif bought_y:
                if ele_y > ele_x:
                    profit_from_trading += thresh
                    bought_y = False 
    if bought_x:
        loss = ele_y - ele_x
    elif bought_y:
        loss = ele_x - ele_y
    else:
        loss = 0

    # logging.info("Profit: {}, Loss: {}".format(profit, loss))

    return {'profit': profit_from_trading - loss,
            'profit_from_trading': profit_from_trading,
            'loss': loss}


def show_plot(result_dict):
    df = pd.DataFrame(result_dict)
    df.plot()
    plt.show()

    
    
        
