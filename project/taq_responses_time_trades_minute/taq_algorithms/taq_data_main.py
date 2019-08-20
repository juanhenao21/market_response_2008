'''
TAQ data main

Script to analyze the TAQ data with the information of 6 stocks during a 2008.

For the first proyect I need to obtain the cross response functions between
individual stocks. To compute these values I need to calculate the midpoint
price, the midpoint log returns and the trade signs. Each task is specified
in each function.

Juan Camilo Henao Londono
juan.henao-londono@stud.uni-due.de
'''
# -----------------------------------------------------------------------------
# Modules

from itertools import product
import subprocess

import multiprocessing as mp
import pickle
import pandas as pd

import taq_data_analysis
import taq_data_plot
import taq_data_tools

__tau__ = 10000

# -----------------------------------------------------------------------------


def main():

    # Tickers and days to analyze

    tickers = ['AAPL', 'MSFT']
    year = '2008'
    taus = [5, 10, 50, 100, 500, 1000]

    with mp.Pool(processes=mp.cpu_count()) as pool:

        pool.starmap(taq_data_analysis.taq_self_response_year_responses_time_trades_minute_data,
                     product(tickers, [year], taus))

        pool.starmap(taq_data_analysis.taq_cross_response_year_responses_time_trades_minute_data,
                     product(tickers, tickers, [year], taus))

        pool.starmap(taq_data_plot.taq_self_response_year_responses_time_trades_minute_plot,
                     product(tickers, [year], taus))
        pool.starmap(taq_data_plot.taq_cross_response_year_responses_time_trades_minute_plot,
                     product(tickers, tickers, [year], taus))

        pool.starmap(taq_data_analysis.taq_self_response_year_avg_responses_time_trades_minute_data,
                     product(tickers, [year], taus))
        pool.starmap(taq_data_analysis.taq_cross_response_year_avg_responses_time_trades_minute_data,
                     product(tickers, tickers, [year], taus))

        pool.starmap(taq_data_plot.taq_self_response_year_avg_responses_time_trades_minute_plot,
                     product(tickers, [year], taus))
        pool.starmap(taq_data_plot.taq_cross_response_year_avg_responses_time_trades_minute_plot,
                     product(tickers, tickers, [year], taus))

        pool.starmap(taq_data_analysis.taq_self_response_year_avg_responses_time_trades_minute_data_v2,
                     product(tickers, [year], taus))
        pool.starmap(taq_data_analysis.taq_cross_response_year_avg_responses_time_trades_minute_data_v2,
                     product(tickers, tickers, [year], taus))

        pool.starmap(taq_data_plot.taq_self_response_year_avg_responses_time_trades_minute_plot_v2,
                     product(tickers, [year], taus))
        pool.starmap(taq_data_plot.taq_cross_response_year_avg_responses_time_trades_minute_plot_v2,
                     product(tickers, tickers, [year], taus))

        print('Ay vamos!!')

    return None

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()