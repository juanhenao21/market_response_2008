'''
ITCH data plot

Module to plot different ITCH results based on the results of the functions
set in the module itch_data_generator. The module plot the following data

- Midpoint price data: plot the midpoint price for every day for a stock in
  one figure.

- Trade signs data: plot the trade signs in a minute of the open market
  (11:00 to 11:01).

- Self response data: plot the self response function for every day for a
  stock in individual plots in one figure.

- Cross response data: plot the cross response function for every day for
  two stock in individual plots in one figure.

- Average return average trade sign return data: plot the product between the
  averaged midpoint log retun and the trade signs for every day for two stocks
  in individual plots in one figure.

- Zero correlation model data: plot the zero correlation model for every day
  for a stock in individual plots in one figure.

- Cross response - average return/sign: plot the cross response function and
  the product of the averaged midpoint log return by the trade signs for every
  day for two stocks in independent figures to compare both results.

- Difference: plot the difference between cross response and average for every
  day for two stocks in individual plots in one figure.

- Self response behavior: plot the self response, the self response absolute
  and the zero correlation model for every day for a stock in independent
  plots in one figure.

- Trade sign cross correlator: plot the trade sign cross correlator for
  every day for two stocks in independent pltos in one figure.

- Trade sign self correlator: plot the trade sign self correlator for
  every day for one stock in independent plots in one figure.

Juan Camilo Henao Londono
juan.henao-londono@stud.uni-due.de
'''

# -----------------------------------------------------------------------------------------------------------------------
# Modules

from matplotlib import pyplot as plt
import os

import pickle

import itch_data_tools

# -----------------------------------------------------------------------------------------------------------------------


def itch_midpoint_plot(ticker, year, month, day, t_step):
    """
    Plot the midpoint price data during a open market day. The data is loaded
    from the mipoint price data results. Function to be used in the function
    midpoint_plot_week.
        :param ticker: string of the abbreviation of the stock to be analized
         (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param day: string of the day to be analized (i.e '07')
        :param t_step: time step in the data in ms
    """

    function_name = itch_midpoint_plot.__name__
    itch_data_tools.itch_function_header_print_plot(function_name, ticker,
                                                    ticker, year, month, day,
                                                    str(t_step))

    # Load data
    midpoint = pickle.load(open(''.join((
                '../itch_data_{1}/itch_midpoint_data_1ms/itch_midpoint_data'
                + '_midpoint_{1}{2}{3}_{0}_1ms.pickle').split())
                .format(ticker, year, month, day), 'rb'))
    time = pickle.load(open(''.join((
                '../itch_data_{}/itch_midpoint_data_1ms/itch_midpoint_data'
                + '_time_1ms.pickle').split())
                .format(year), 'rb'))

    # Plotting

    plt.plot(time[::100] / 1000 / 3600, midpoint[::100],
             label=('Day {}'.format(day)))
    plt.legend(loc=0, fontsize=20)

    return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_midpoint_week_plot(ticker, year, month, days, t_step):
    """
    Plot the midpoint price data during a time period. The data is loaded from
    the mipoint price data results. The time period must be previously knowed
    and set to the function.
        :param ticker: string of the abbreviation of the stock to be analized
         (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param days: string with the days to be analized
         (i.e ['07', '08', '09'])
        :param t_step: time step in the data in ms
    """

    figure = plt.figure(figsize=(16, 9))

    for day in days:
        itch_midpoint_plot(ticker, year, month, day, t_step)

    plt.title('{}'.format(ticker), fontsize=40)
    plt.xlabel(r'Time $[hour]$', fontsize=25)
    plt.ylabel(r'Price $ [\$] $', fontsize=25)
    plt.tight_layout()
    plt.grid(True)

    # Plotting
    function_name = itch_midpoint_week_plot.__name__
    itch_data_tools.itch_save_plot(function_name, figure, ticker, ticker, year,
                                   month, str(t_step))

    return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_ask_bid_midpoint_spread_plot(ticker, year, month, day, t_step):
    """
    Plot the ask, bid, midpoint price and spread data during a open market
    day. The data is loaded from the mipoint price data results.
        :param ticker: string of the abbreviation of the stock to be analized
         (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param day: string of the day to be analized (i.e '07')
        :param t_step: time step in the data in ms
    """

    function_name = itch_ask_bid_midpoint_spread_plot.__name__
    itch_data_tools.itch_function_header_print_plot(function_name, ticker,
                                                    ticker, year, month, day,
                                                    str(t_step))

    # Load data
    ask = pickle.load(open(''.join((
                '../itch_data_{1}/itch_midpoint_data_1ms/itch_midpoint_data'
                + '_ask_{1}{2}{3}_{0}_1ms.pickle').split())
                .format(ticker, year, month, day), 'rb'))
    bid = pickle.load(open(''.join((
                '../itch_data_{1}/itch_midpoint_data_1ms/itch_midpoint_data'
                + '_bid_{1}{2}{3}_{0}_1ms.pickle').split())
                .format(ticker, year, month, day), 'rb'))
    midpoint = pickle.load(open(''.join((
                '../itch_data_{1}/itch_midpoint_data_1ms/itch_midpoint_data'
                + '_midpoint_{1}{2}{3}_{0}_1ms.pickle').split())
                .format(ticker, year, month, day), 'rb'))
    spread = pickle.load(open(''.join((
                '../itch_data_{1}/itch_midpoint_data_1ms/itch_midpoint_data'
                + '_spread_{1}{2}{3}_{0}_1ms.pickle').split())
                .format(ticker, year, month, day), 'rb'))
    time = pickle.load(open(''.join((
                '../itch_data_{}/itch_midpoint_data_1ms/itch_midpoint_data'
                + '_time_1ms.pickle').split())
                .format(year), 'rb'))

    figure = plt.figure(figsize=(9, 16))
    figure.suptitle('{} - {}.{}.{}'.format(ticker, year, month, day),
                    fontsize=16)
    figure.tight_layout()
    figure.subplots_adjust(top=0.95, wspace=0.3)

    plt.subplot(4, 2, 1)
    plt.plot(time[::100] / 1000 / 3600, midpoint[::100], label='Midpoint')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.grid(True)

    plt.subplot(4, 2, 2)
    plt.plot(time[500::100] / 1000 / 3600, spread[500::100], label='Spread')
    plt.xlabel('Time')
    plt.ylabel('Spread')
    plt.legend(loc='best')
    plt.ylim(0, 0.1)
    plt.grid(True)

    plt.subplot(4, 2, 3)
    plt.plot(time[::100] / 1000 / 3600, bid[::100], label='Bid quotes')
    plt.plot(time[::100] / 1000 / 3600, ask[::100], label='Ask quotes')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.grid(True)

    plt.subplot(4, 2, 4)
    plt.scatter(time[::100] / 1000 / 3600, ask[::100], marker='.', s=5,
                label='Ask trades')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.grid(True)

    # Saving data

    if (not os.path.isdir('../itch_plot_{1}/{0}_{2}ms/'
                          .format(function_name, year, t_step))):

        try:

            os.mkdir('../itch_plot_{1}/{0}_{2}ms/'
                     .format(function_name, year, t_step))
            print('Folder to save data created')

        except FileExistsError:

            print('Folder exists. The folder was not created')

    figure.savefig(
            '../itch_plot_{2}/{0}_{4}ms/{0}_{2}{3}_{1}i_{4}ms.png'
            .format(function_name, ticker, year, month, str(t_step)))

    print('Plot saved')
    print()

    return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_trade_signs_plot(ticker, year, month, day, t_step):
    """
    Plot the trade signs data during one minute (11:00 to 11:01) in one day for
    a ticker. The data is loaded from the trade signs data results.
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param day: string of the day to be analized (i.e '07')
        :param t_step: time step in the data in ms
    """

    function_name = itch_trade_signs_plot.__name__
    itch_data_tools.itch_function_header_print_plot(function_name, ticker,
                                                    ticker, year, month, day,
                                                    str(t_step))

    # Load data

    trade_signs = pickle.load(open("".join((
                '../itch_data_{1}/itch_trade_signs_data_1ms/itch_trade_signs'
                + '_data_{1}{2}{3}_{0}_1ms.pickle').split())
                .format(ticker, year, month, day), 'rb'))
    time = pickle.load(open(''.join((
                '../itch_data_{}/itch_midpoint_data_1ms/itch_midpoint_data'
                + '_time_1ms.pickle').split())
                .format(year), 'rb'))

    figure = plt.figure(figsize=(16, 9))

    plt.plot(time[5399964:5457598] / 1000 / 3600,
             trade_signs[5399964:5457598], '-g',
             label='Trade signs using the majority')
    plt.title('Trade signs {}'.format(ticker), fontsize=40)
    plt.xlabel(r'Time $[hour]$', fontsize=25)
    plt.ylabel(r'Buy $(+1)$ or Sell $(-1)$', fontsize=25)
    plt.legend(loc='best', fontsize=20)

    plt.tight_layout()

    # Plotting
    itch_data_tools.itch_save_plot(function_name, figure, ticker, ticker, year,
                                   month, str(t_step))

    return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_self_response_plot(ticker, year, month, days, t_step):
    """
    Plot the self response during an interval of time (days) in independent
    plots in a figure. The data is loaded from the self response data results.
        :param ticker: string of the abbreviation of the stock to be analized
         (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param day: string of the day to be analized (i.e '07')
        :param t_step: time step in the data in ms
    """

    figure = plt.figure(figsize=(9, 16))
    plt.subplots_adjust(hspace=0, wspace=0)

    for i, day in enumerate(days):

        function_name = itch_self_response_plot.__name__
        itch_data_tools.itch_function_header_print_plot(function_name, ticker,
                                                        ticker, year, month,
                                                        day, str(t_step))

        plot = pickle.load(open(''.join((
            '../itch_data_{1}/itch_self_response_data_{4}ms/itch_self_response'
            + '_data_{1}{2}{3}_{0}_{4}ms.pickle').split())
            .format(ticker, year, month, day, t_step), 'rb'))

        plt.subplot(len(days), 1, i+1)
        plt.semilogx(plot, '-g', label='Stock i {} - Day {}'
                     .format(ticker, day))
        plt.xlabel(r'Time lag $[\tau]$')
        plt.ylabel(r'Self response $ R_{ii} (\tau) $')
        plt.legend(loc='best')
        plt.title('Self response - {} - {}ms'.format(ticker, t_step))
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        plt.grid(True)
        plt.tight_layout()

    # Plotting
    itch_data_tools.itch_save_plot(function_name, figure, ticker, ticker, year,
                                   month, str(t_step))

    return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_self_response_abs_plot(ticker, year, month, days, t_step):
    """
    Plot the self response absolute during an interval of time (days) in
    independent plots in a figure. The data is loaded from the self response
    data results.
        :param ticker: string of the abbreviation of the stock to be analized
         (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param day: string of the day to be analized (i.e '07')
        :param t_step: time step in the data in ms
    """

    figure = plt.figure(figsize=(9, 16))
    plt.subplots_adjust(hspace=0, wspace=0)

    for i, day in enumerate(days):

        function_name = itch_self_response_abs_plot.__name__
        itch_data_tools.itch_function_header_print_plot(function_name, ticker,
                                                        ticker, year, month,
                                                        day, str(t_step))

        plot = pickle.load(open(''.join((
            '../itch_data_{1}/itch_self_response_abs_data_{4}ms/itch_self_'
            + 'response_abs_data_{1}{2}{3}_{0}_{4}ms.pickle').split())
            .format(ticker, year, month, day, t_step), 'rb'))

        plt.subplot(len(days), 1, i+1)
        plt.semilogx(plot, '-g', label='Stock i {} - Day {}'
                     .format(ticker, day))
        plt.xlabel(r'Time lag $[\tau]$')
        plt.ylabel(r'Self response $ R_{ii} (\tau) $')
        plt.legend(loc='best')
        plt.title('Self response absolute - {} - {}ms'.format(ticker, t_step))
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        plt.grid(True)
        plt.tight_layout()

    # Plotting
    itch_data_tools.itch_save_plot(function_name, figure, ticker, ticker, year,
                                   month, str(t_step))

    return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_zero_correlation_model_plot(ticker, year, month, days, t_step):
    """
    Plot the zero correlation model during an interval of time (days) in
    independent plots in a figure. The data is loaded from the zero
    correlation model data results.
        :param ticker: string of the abbreviation of the midpoint stock to
         be analized (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param day: string of the day to be analized (i.e '07')
        :param t_step: time step in the data in ms
    """
    figure = plt.figure(figsize=(9, 16))
    plt.subplots_adjust(hspace=0, wspace=0)

    for d, day in enumerate(days):

        function_name = itch_zero_correlation_model_plot.__name__
        itch_data_tools.itch_function_header_print_plot(function_name, ticker,
                                                        ticker, year, month,
                                                        day, str(t_step))

        plot = pickle.load(open(''.join((
            '../itch_data_{1}/itch_zero_correlation_model_data_{4}ms/itch'
            + '_zero_correlation_model_data_{1}{2}{3}_{0}_{4}ms.pickle')
            .split()).format(ticker, year, month, day, t_step), 'rb'))

        plt.subplot(5, 1, d+1)
        plt.semilogx(plot, '-g', label='Stock i {} and random trade sign - {}'
                     .format(ticker, day))
        plt.xlabel(r'Time lag $[\tau]$')
        plt.ylabel(r'Self response random $ R_{ii} (\tau)_{rand} $')
        plt.title('Zero correlation - ticker i {} - {}ms'
                  .format(ticker, t_step))
        plt.legend(loc='best')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        plt.grid(True)
        plt.tight_layout()

    # Plotting
    itch_data_tools.itch_save_plot(function_name, figure, ticker, ticker, year,
                                   month, str(t_step))

    return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_self_response_self_abs_zero_corr_plot(ticker, year, month, days,
                                               t_step):
    """
    Plot the self response, self response absolute and zero correlation model
    during an interval of time (days) in independent plots in a figure. The
    data is loaded from the self response data results, the self response
    absolute data results and zero correlation model data results.
        :param ticker: string of the abbreviation of the midpoint stock to
         be analized (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param days: string with the days to be analized
         (i.e ['07', '08', '09'])
        :param t_step: time step in the data in ms
    """

    figure = plt.figure(figsize=(9, 16))
    plt.subplots_adjust(hspace=0, wspace=0)

    for d, day in enumerate(days):

        function_name = itch_self_response_self_abs_zero_corr_plot.__name__
        itch_data_tools.itch_function_header_print_plot(function_name, ticker,
                                                        ticker, year, month,
                                                        day, str(t_step))

        self_ = pickle.load(open(''.join((
            '../itch_data_{1}/itch_self_response_data_{4}ms/itch_self_response'
            + '_data_{1}{2}{3}_{0}_{4}ms.pickle').split())
            .format(ticker, year, month, day, t_step), 'rb'))
        abs_ = pickle.load(open(''.join((
            '../itch_data_{1}/itch_self_response_abs_data_{4}ms/itch_self_'
            + 'response_abs_data_{1}{2}{3}_{0}_{4}ms.pickle').split())
            .format(ticker, year, month, day, t_step), 'rb'))
        zero = pickle.load(open(''.join((
            '../itch_data_{1}/itch_zero_correlation_model_data_{4}ms/itch'
            + '_zero_correlation_model_data_{1}{2}{3}_{0}_{4}ms.pickle')
            .split()).format(ticker, year, month, day, t_step), 'rb'))

        plt.subplot(len(days), 1, d+1)
        plt.semilogx(self_, '-', label='Self response Stock i {} - {}'
                     .format(ticker, day))
        plt.semilogx(abs_, '-', label='Self response abs Stock i {} - {}'
                     .format(ticker, day))
        plt.semilogx(zero, '-', label='Zero correlation Stock i {} - {}'
                     .format(ticker, day))
        plt.xlabel(r'Time lag $[\tau]$')
        plt.ylabel(r'Self response $ R_{ii} (\tau) $')
        plt.legend(loc='best')
        plt.title('Self res - abs - zero - {}i - {}ms'
                  .format(ticker, t_step))
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        plt.grid(True)
        plt.tight_layout()

    # Plotting
    itch_data_tools.itch_save_plot(function_name, figure, ticker, ticker, year,
                                   month, str(t_step))

    return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_cross_response_plot(ticker_i, ticker_j, year, month, days, t_step):
    """
    Plot the cross response during an interval of time (days) in independent
    plots in a figure. The data is loaded from the cross response data results.
        :param ticker_i: string of the abbreviation of the midpoint stock to
         be analized (i.e. 'AAPL')
        :param ticker_j: string of the abbreviation of the midpoint stock to
         be analized (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param days: string with the days to be analized
         (i.e ['07', '08', '09'])
        :param t_step: time step in the data in ms
    """

    if (ticker_i == ticker_j):

        return None

    else:

        figure = plt.figure(figsize=(9, 16))
        plt.subplots_adjust(hspace=0, wspace=0)

        for i, day in enumerate(days):

            function_name = itch_cross_response_plot.__name__
            itch_data_tools.itch_function_header_print_plot(function_name,
                                                            ticker_i, ticker_j,
                                                            year, month, day,
                                                            str(t_step))

            plot = pickle.load(open(''.join((
                '../itch_data_{2}/itch_cross_response_data_{5}ms/itch_cross'
                + '_response_data_{2}{3}{4}_{0}i_{1}j_{5}ms.pickle').split())
                .format(ticker_i, ticker_j, year, month, day, t_step), 'rb'))

            plt.subplot(len(days), 1, i+1)
            plt.semilogx(plot, '-g', label='Stock i {} - Stock j {} - Day {}'
                         .format(ticker_i, ticker_j, day))
            plt.xlabel(r'Time lag $[\tau]$')
            plt.ylabel(r'Cross response $ R_{ij} (\tau) $')
            plt.legend(loc='best')
            plt.title('Cross response - ticker i {} ticker j {} - {}ms'
                      .format(ticker_i, ticker_j, t_step))
            plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
            plt.grid(True)
            plt.tight_layout()

        # Plotting
        itch_data_tools.itch_save_plot(function_name, figure, ticker_i,
                                       ticker_j, year, month, str(t_step))

        return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_avg_return_avg_trade_prod_plot(ticker_i, ticker_j, year, month, days,
                                        t_step):
    """
    Plot the average midpoint log return price multiplied by the average trade
    signs during an interval of time (days) in independent plots in a figure.
    The data is loaded from the averaged data results.
        :param ticker_i: string of the abbreviation of the midpoint stock to
         be analized (i.e. 'AAPL')
        :param ticker_j: string of the abbreviation of the midpoint stock to
         be analized (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param days: string with the days to be analized
         (i.e ['07', '08', '09'])
        :param t_step: time step in the data in ms
    """

    if (ticker_i == ticker_j):

        return None

    else:

        figure = plt.figure(figsize=(9, 16))
        plt.subplots_adjust(hspace=0, wspace=0)

        for i, day in enumerate(days):

            function_name = itch_avg_return_avg_trade_prod_plot.__name__
            itch_data_tools.itch_function_header_print_plot(function_name,
                                                            ticker_i, ticker_j,
                                                            year, month, day,
                                                            str(t_step))

            plot = pickle.load(open(''.join((
                '../itch_data_{2}/itch_avg_return_avg_trade_prod_data_{5}ms/'
                + 'itch_avg_return_avg_trade_prod_data_{2}{3}{4}_{0}i_{1}j_'
                + '{5}ms.pickle').split())
                .format(ticker_i, ticker_j, year, month, day, t_step), 'rb'))

            plt.subplot(len(days), 1, i+1)
            plt.semilogx(plot, '-g', label='Stock i {} - Stock j {} - Day {}'
                         .format(ticker_i, ticker_j, day))
            plt.xlabel(r'Time lag $[\tau]$')
            plt.ylabel("".join((
                       r'$ \left \langle r_{i}\left ( t, \tau \right )'
                       + r'\right \rangle \left \langle \epsilon_{j} \left ( t'
                       + r'\right ) \right \rangle $').split()))
            plt.legend(loc='best')
            plt.title('Average - ticker i {} ticker j {} - {}ms'
                      .format(ticker_i, ticker_j, t_step))
            plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
            plt.grid(True)
            plt.tight_layout()

        # Plotting
        itch_data_tools.itch_save_plot(function_name, figure, ticker_i,
                                       ticker_j, year, month, str(t_step))

        return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_cross_response_avg_return_avg_trade_plot(ticker_i, ticker_j, year,
                                                  month, days, t_step):
    """
    Plot the cross response and the avg return and trade  during an interval
    of time (days) in independent plots in a figure to compare the behavior of
    both results. The data is loaded from the cross response data results and
    the average return and average trade sign data results.
        :param ticker_i: string of the abbreviation of the midpoint stock to
         be analized (i.e. 'AAPL')
        :param ticker_j: string of the abbreviation of the midpoint stock to
         be analized (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param days: string with the days to be analized
         (i.e ['07', '08', '09'])
        :param t_step: time step in the data in ms
    """

    if (ticker_i == ticker_j):

        return None

    else:

        figure = plt.figure(figsize=(9, 16))
        plt.subplots_adjust(hspace=0, wspace=0)

        for i, day in enumerate(days):

            function_name = itch_cross_response_avg_return_avg_trade_plot.\
                            __name__
            itch_data_tools.itch_function_header_print_plot(function_name,
                                                            ticker_i, ticker_j,
                                                            year, month, day,
                                                            str(t_step))

            cross = pickle.load(open(''.join((
                '../itch_data_{2}/itch_cross_response_data_{5}ms/itch_cross'
                + '_response_data_{2}{3}{4}_{0}i_{1}j_{5}ms.pickle').split())
                .format(ticker_i, ticker_j, year, month, day, t_step), 'rb'))
            avg = pickle.load(open(''.join((
                '../itch_data_{2}/itch_avg_return_avg_trade_prod_data_{5}ms/'
                + 'itch_avg_return_avg_trade_prod_data_{2}{3}{4}_{0}i_{1}j_'
                + '{5}ms.pickle').split())
                .format(ticker_i, ticker_j, year, month, day, t_step), 'rb'))

            plt.subplot(len(days), 2, 2*i+1)
            plt.semilogx(cross, '-g', label='Stock i {} and stock j {} - {}'
                         .format(ticker_i, ticker_j, day))
            plt.xlabel(r'Time lag $[\tau]$')
            plt.ylabel(r'Cross response $ R_{ij} (\tau) $')
            plt.legend(loc='best')
            plt.title('Cross - {}i - {}j - {}ms'
                      .format(ticker_i, ticker_j, t_step))
            plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
            plt.grid(True)
            plt.tight_layout()

            plt.subplot(len(days), 2, 2*i+2)
            plt.semilogx(avg, '-g', label='Stock i {} and stock j {} - {}'
                         .format(ticker_i, ticker_j, day))
            plt.xlabel(r'Time lag $[\tau]$')
            plt.ylabel("".join((
                       r'$ \left \langle r_{i}\left ( t, \tau \right )'
                       + r'\right \rangle \left \langle \epsilon_{j} \left ( t'
                       + r'\right ) \right \rangle $').split()))
            plt.legend(loc='best')
            plt.title('Avg - {}i - {}j - {}ms'
                      .format(ticker_i, ticker_j, t_step))
            plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
            plt.grid(True)
            plt.tight_layout()

        # Plotting
        itch_data_tools.itch_save_plot(function_name, figure, ticker_i,
                                       ticker_j, year, month, str(t_step))

        return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_difference_cross_response_avg_prod_plot(ticker_i, ticker_j, year,
                                                 month, days, t_step):
    """
    Plot the cross response and average product during an interval of time
    (days) in independent plots in a figure. The data is loaded from the cross
    response data results and the average data results.
        :param ticker_i: string of the abbreviation of the midpoint stock to
         be analized (i.e. 'AAPL')
        :param ticker_j: string of the abbreviation of the midpoint stock to
         be analized (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param days: string with the days to be analized
         (i.e ['07', '08', '09'])
        :param t_step: time step in the data in ms
    """

    if (ticker_i == ticker_j):

        return None

    else:

        figure = plt.figure(figsize=(9, 16))
        plt.subplots_adjust(hspace=0, wspace=0)

        for i, day in enumerate(days):

            function_name = itch_difference_cross_response_avg_prod_plot.\
                            __name__
            itch_data_tools.itch_function_header_print_plot(function_name,
                                                            ticker_i, ticker_j,
                                                            year, month, day,
                                                            str(t_step))

            plot_cross = pickle.load(open(''.join((
                '../itch_data_{2}/itch_cross_response_data_{5}ms/itch_cross'
                + '_response_data_{2}{3}{4}_{0}i_{1}j_{5}ms.pickle').split())
                .format(ticker_i, ticker_j, year, month, day, t_step), 'rb'))

            plot_avg = pickle.load(open(''.join((
                '../itch_data_{2}/itch_avg_return_avg_trade_prod_data_{5}ms/'
                + 'itch_avg_return_avg_trade_prod_data_{2}{3}{4}_{0}i_{1}j_'
                + '{5}ms.pickle').split())
                .format(ticker_i, ticker_j, year, month, day, t_step), 'rb'))

            plot_diff = pickle.load(open(''.join((
                '../itch_data_{2}/itch_difference_cross_response_avg_prod_'
                + 'data_{5}ms/itch_difference_cross_response_avg_prod_data_'
                + '{2}{3}{4}_{0}i_{1}j_{5}ms.pickle').split())
                .format(ticker_i, ticker_j, year, month, day, t_step), 'rb'))

            plt.subplot(len(days), 1, i+1)
            plt.semilogx(plot_cross, '-',
                         label=''.join(('Cross response Stock i {} - '
                                       + 'Stock j {} - Day {}').split())
                         .format(ticker_i, ticker_j, day))
            plt.semilogx(plot_avg, '-',
                         label=''.join(('Average product Stock i {} - '
                                       + 'Stock j {} - Day {}').split())
                         .format(ticker_i, ticker_j, day))
            plt.semilogx(plot_diff, '-g',
                         label='Difference Stock i {} - Stock j {} - Day {}'
                         .format(ticker_i, ticker_j, day))
            plt.xlabel(r'Time lag $[\tau]$')
            plt.ylabel(r'Response')
            plt.legend(loc='best')
            plt.title('Difference response - ticker i {} ticker j {} - {}ms'
                      .format(ticker_i, ticker_j, t_step))
            plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
            plt.grid(True)
            plt.tight_layout()

        # Plotting
        itch_data_tools.itch_save_plot(function_name, figure, ticker_i,
                                       ticker_j, year, month, str(t_step))

        return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_trade_sign_self_correlator_plot(ticker, year, month, days, t_step):
    """
    Plot the trade sign self correlator during an interval of time (days) in
    independent plots in a figure. The data is loaded from the trade sign self
    correlator data results.
        :param ticker: string of the abbreviation of the trade sign stock to
         be analized (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param days: string with the days to be analized
         (i.e ['07', '08', '09'])
        :param t_step: time step in the data in ms
    """

    figure = plt.figure(figsize=(9, 16))
    plt.subplots_adjust(hspace=0, wspace=0)

    for i, day in enumerate(days):

        function_name = itch_trade_sign_self_correlator_plot.__name__
        itch_data_tools.itch_function_header_print_plot(function_name, ticker,
                                                        ticker, year, month,
                                                        day, str(t_step))

        plot = pickle.load(open(''.join((
            '../itch_data_{1}/itch_trade_sign_self_correlator_data_{4}ms/'
            + 'itch_trade_sign_self_correlator_data_{1}{2}{3}_{0}_{4}ms'
            + '.pickle').split())
            .format(ticker, year, month, day, t_step), 'rb'))

        plt.subplot(len(days), 1, i+1)
        plt.loglog(plot, '-g', label='Stock i {} - Day {}'
                   .format(ticker, day))
        plt.xlabel(r'Time lag $[\tau]$')
        plt.ylabel(r'Trade sign self correlator $ \Theta_{ii} (\tau) $')
        plt.legend(loc='best')
        plt.title('Trade sign self correlator - ticker i {} - {}ms'
                  .format(ticker, t_step))
        plt.ylim([10E-6, 10])
        plt.grid(True)
        plt.tight_layout()

    # Plotting
    itch_data_tools.itch_save_plot(function_name, figure, ticker, ticker, year,
                                   month, str(t_step))

    return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_trade_sign_autocorrelation_plot(ticker, year, month, days, t_step):
    """
    Plot the trade sign autocorrelation during an interval of time (days) in
    independent plots in a figure. The data is loaded from the trade sign
    autocorrelation data results.
        :param ticker: string of the abbreviation of the trade sign stock to
         be analized (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param days: string with the days to be analized
         (i.e ['07', '08', '09'])
        :param t_step: time step in the data in ms
    """

    figure = plt.figure(figsize=(9, 16))
    plt.subplots_adjust(hspace=0, wspace=0)

    for i, day in enumerate(days):

        function_name = itch_trade_sign_autocorrelation_plot.__name__
        itch_data_tools.itch_function_header_print_plot(function_name, ticker,
                                                        ticker, year, month,
                                                        day, str(t_step))

        plot = pickle.load(open(''.join((
            '../itch_data_{1}/itch_trade_sign_autocorrelation_data_{4}ms/'
            + 'itch_trade_sign_autocorrelation_data_{1}{2}{3}_{0}_{4}ms'
            + '.pickle').split())
            .format(ticker, year, month, day, t_step), 'rb'))

        plt.subplot(len(days), 1, i+1)
        plt.loglog(plot, '-g', label='Stock i {} - Day {}'
                   .format(ticker, day))
        plt.xlabel(r'Time lag $[\tau]$')
        plt.ylabel(r'Trade sign autocorrelation')
        plt.legend(loc='best')
        plt.title(
            'Trade sign autocorrelation - ticker i {} - {}ms'
            .format(ticker, t_step))
        plt.ylim([10E-6, 10])
        plt.grid(True)
        plt.tight_layout()

    # Plotting
    itch_data_tools.itch_save_plot(function_name, figure, ticker, ticker, year,
                                   month, str(t_step))

    return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_trade_sign_self_correlator_autocorrelation_plot(ticker, year, month,
                                                         days, t_step):
    """
    Plot the trade sign autocorrelation during an interval of time (days) in
    independent plots in a figure. The data is loaded from the trade sign
    autocorrelation data results.
        :param ticker: string of the abbreviation of the trade sign stock to
         be analized (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param days: string with the days to be analized
         (i.e ['07', '08', '09'])
        :param t_step: time step in the data in ms
    """

    figure = plt.figure(figsize=(9, 16))
    plt.subplots_adjust(hspace=0, wspace=0)

    for i, day in enumerate(days):

        function_name = itch_trade_sign_self_correlator_autocorrelation_plot.\
                        __name__
        itch_data_tools.itch_function_header_print_plot(function_name, ticker,
                                                        ticker, year, month,
                                                        day, str(t_step))

        plot_self_correlator = pickle.load(open(''.join((
            '../itch_data_{1}/itch_trade_sign_self_correlator_data_{4}ms/'
            + 'itch_trade_sign_self_correlator_data_{1}{2}{3}_{0}_{4}ms'
            + '.pickle').split())
            .format(ticker, year, month, day, t_step), 'rb'))

        plot_autocorrelation = pickle.load(open(''.join((
            '../itch_data_{1}/itch_trade_sign_autocorrelation_data_{4}ms/'
            + 'itch_trade_sign_autocorrelation_data_{1}{2}{3}_{0}_{4}ms'
            + '.pickle').split())
            .format(ticker, year, month, day, t_step), 'rb'))

        plt.subplot(len(days), 1, i+1)
        plt.loglog(plot_self_correlator, '-',
                   label='Self correlator {} - Day {}'
                   .format(ticker, day))
        plt.loglog(plot_autocorrelation, '-',
                   label='Autocorrelation {} - Day {}'
                   .format(ticker, day))
        plt.xlabel(r'Time lag $[\tau]$')
        plt.ylabel(r'Trade sign autocorrelation - self correlator')
        plt.legend(loc='best')
        plt.title(
            'Trade sign self correlator - autocorrelation - ticker i {} - {}ms'
            .format(ticker, t_step))
        plt.ylim([10E-6, 10])
        plt.grid(True)
        plt.tight_layout()

    # Plotting
    itch_data_tools.itch_save_plot(function_name, figure, ticker, ticker, year,
                                   month, str(t_step))

    return None

# -----------------------------------------------------------------------------------------------------------------------


def itch_trade_sign_cross_correlator_plot(ticker_i, ticker_j, year, month,
                                          days, t_step):
    """
    Plot the trade sign cross correlator during an interval of time (days) in
    independent plots in a figure. The data is loaded from the trade sign cross
    correlator data results.
        :param ticker_i: string of the abbreviation of the trade sign stock to
         be analized (i.e. 'AAPL')
        :param ticker_j: string of the abbreviation of the trade sign stock to
         be analized (i.e. 'AAPL')
        :param year: string of the year to be analized (i.e '2008')
        :param month: string of the month to be analized (i.e '07')
        :param days: string with the days to be analized
         (i.e ['07', '08', '09'])
        :param t_step: time step in the data in ms
    """

    if (ticker_i == ticker_j):

        return None

    else:

        figure = plt.figure(figsize=(9, 16))
        plt.subplots_adjust(hspace=0, wspace=0)

        for i, day in enumerate(days):

            function_name = itch_trade_sign_cross_correlator_plot.__name__
            itch_data_tools.itch_function_header_print_plot(function_name,
                                                            ticker_i, ticker_j,
                                                            year, month, day,
                                                            str(t_step))

            plot = pickle.load(open(''.join((
                '../itch_data_{2}/itch_trade_sign_cross_correlator_data_{5}ms'
                + '/itch_trade_sign_cross_correlator_data_{2}{3}{4}_{0}i_{1}j'
                + '_{5}ms.pickle').split())
                .format(ticker_i, ticker_j, year, month, day, t_step), 'rb'))

            plt.subplot(len(days), 1, i+1)
            plt.loglog(plot, '-g', label='Stock i {} - Stock j {} - Day {}'
                       .format(ticker_i, ticker_j, day))
            plt.xlabel(r'Time lag $[\tau]$')
            plt.ylabel(r'Trade sign cross correlator $ \Theta_{ij} (\tau) $')
            plt.legend(loc='best')
            plt.title(
                'Trade sign cross correlator - ticker i {} ticker j {} - {}ms'
                .format(ticker_i, ticker_j, t_step))
            plt.ylim([10E-6, 10])
            plt.grid(True)
            plt.tight_layout()

        # Plotting
        itch_data_tools.itch_save_plot(function_name, figure, ticker_i,
                                       ticker_j, year, month, str(t_step))

        return None

# -----------------------------------------------------------------------------------------------------------------------


def main():

    return None

# -----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    main()