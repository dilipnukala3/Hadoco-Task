import numpy as np
import pandas as pd

MIN_PURCHASES = 6


def get_ipt(tran : pd.DataFrame) :
    
    tran['date']= pd.to_datetime(tran['transaction_date'], format='%Y-%m-%d')
    tran['year'] = tran['date'].astype(str).str[:4]
    tran['previous_visit'] = tran.groupby(['cust_id'])['date'].shift()
    tran['days_bw_visits'] = tran['date'] - tran['previous_visit']
    tran['days_bw_visits'] = tran['days_bw_visits'].apply(lambda x: x.days)
    return tran.groupby(['cust_id'])['days_bw_visits'].median().values[0]


class CustomerInfo:
    """
    Attributes:
        - transactions: Contains the transaction history of a customer
        (TODO 1.1)
        - ipt           - The median interpurchase time or time between two transactions
    """
    transactions: pd.DataFrame
    # TODO 1.1
    ipt: float

    def __init__(self, transactions: pd.DataFrame):
        self.transactions = transactions
        self.ipt = get_ipt(self.transactions)
