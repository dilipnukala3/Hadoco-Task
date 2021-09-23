import datetime as dt

import pandas as pd
import numpy as np
import sys

sys.path.append("../tasks")

from tasks.customer_info_1 import CustomerInfo 

# TODO 2

def get_conditional_last_transaction( transactions : pd.DataFrame, last_date : dt.date, ipt :float, IPT_FACTOR : int):
    days = ipt*IPT_FACTOR
    last_date = np.datetime64(dt.datetime(
                        year = last_date.year,
                        month = last_date.month,
                        day = last_date.day))
    top_date = last_date - np.timedelta64(int(2*days),'D')
    bottom_date = last_date - np.timedelta64(int(days),'D')
    tran = transactions[(transactions['date'] >= top_date)
            & (transactions['date'] <= bottom_date)]
    if tran['date'].count() != 0 :
        a = tran[tran['revenue'] == tran['revenue'].max()]['date']
        return (a[-1].to_pydatetime().date())
    else :
        a = transactions[(transactions['date']<=bottom_date)]['date'][-1]
        return (a.to_pydatetime().date())

def get_daily_revenue_median(transactions : pd.DataFrame,
                            last_transaction_date : dt.date):
    last_transaction_date = np.datetime64(dt.datetime(
                        year = last_transaction_date.year,
                        month = last_transaction_date.month,
                        day = last_transaction_date.day))
    
    tran = transactions[transactions['date'] <= last_transaction_date]
    tran['prev_date'] = tran['date'].shift(-1)
    tran['in_between_days'] = (tran['prev_date'] - tran['date']).apply(lambda x : x.days)
    tran['mean_revenue'] = tran['revenue']/tran['in_between_days']
    return tran['mean_revenue'][:-1].median()

def get_revenue_made_after_last_transaction(
        transactions : pd.DataFrame , 
        last_transaction_date : dt.date) :

    last_transaction_date = np.datetime64(dt.datetime(
                        year = last_transaction_date.year,
                        month = last_transaction_date.month,
                        day = last_transaction_date.day))

    rev_made = transactions[transactions['date'] >= last_transaction_date]["revenue"].sum()
    return rev_made

class ExpectedCustomerBehavior:
    """
    Calculate the expected behavior of a customer
    ---
    Attributes:
        - IPT_FACTOR                    - the factor to define the timeframe for the expected behavior
        - transactions                  - contains the customer transaction data
        - last_date                     - the last (possible) available date in the **data set**

        (TODO 2.1)
        - last_transaction_date         - The time until which the data will be considered to calculate
                                          the expected behavior of the **customer**
        (TODO 2.2)
        - expected_daily_rev            - Calculated after slicicng the transactions until the <last_transaction_date>
                                          The expected daily rev is either
                                            a) the median value
                                            b) the .5 quantile of a fitted probability distribution function

        (TODO: 2.3)
        - expected_rev_until_last_date  - take the revenue from <last_transaction_date> onward
                                          and subtract for every day until <last_date> the daily_rev_hat

        (TODO: 2.4)
        - rev_made                      - the revenue the customer has made in the timeframe between
                                          ipt*IPT_FACTOR
    """
    IPT_FACTOR = 3
    transactions: pd.DataFrame
    last_date: dt.date


    # TODO 2.2:
    last_transaction_date: dt.date


    # TODO 2.1:
    expected_daily_rev: float
    # TODO 2.3:
    expected_rev_until_last_date: int
    # TODO 2.4
    rev_made: int

    def __init__(self,
                 transactions: pd.DataFrame,
                 last_date: dt.date):
        self.transactions = transactions
        self.last_date = last_date

        customer_info = CustomerInfo(self.transactions)
        ipt = customer_info.ipt
        # ########################
        # Your code goes here...
        # ########################
        self.last_transaction_date = get_conditional_last_transaction(
                self.transactions,
                self.last_date,
                ipt,
                ExpectedCustomerBehavior.IPT_FACTOR)#dt.date(2000, 1, 1)
        self.expected_daily_rev = get_daily_revenue_median(
                self.transactions,
                self.last_transaction_date)

        

        self.expected_rev_until_last_date = (self.last_date - self.last_transaction_date).days*self.expected_daily_rev
        self.rev_made = get_revenue_made_after_last_transaction(self.transactions , self.last_transaction_date)


