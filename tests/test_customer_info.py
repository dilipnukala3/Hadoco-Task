import os
import sys

import pandas as pd
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tasks.customer_info_1 import CustomerInfo
from tests.test_initial import transactions, ipts


def test_customer_ipt_exact_match(transactions, ipts):
    transactions = transactions
    ipts = ipts
    cust_ids = transactions.index.unique()
    for cust_id in cust_ids:
        cust_transactions = transactions.loc[cust_id]
        cust_info = CustomerInfo(cust_transactions)
        assert cust_info.ipt == ipts.loc[cust_id].ipt, "IPT Doesn't match"


def test_customer_ipt_almost_match(transactions, ipts):
    transactions = transactions
    ipts = ipts

    cust_ids = transactions.index.unique()
    for cust_id in cust_ids:
        cust_transactions = transactions.loc[cust_id]
        cust_info = CustomerInfo(cust_transactions)
        assert abs(
            (cust_info.ipt - ipts.loc[cust_id].ipt) /
            ipts.loc[cust_id].ipt
        ) < .15, "The difference between the IPTs is > 15%"