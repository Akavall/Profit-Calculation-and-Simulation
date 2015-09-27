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
            logging.info("Broke up on: {}".format(i))

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

def show_plot(result_dict):
    df = pd.DataFrame(result_dict)
    df.plot()
    plt.show()
    
    
        
