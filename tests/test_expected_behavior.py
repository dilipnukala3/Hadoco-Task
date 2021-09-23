import os
import sys
import datetime as dt
from math import floor

import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tests.test_initial import last_transaction_date, transactions, expected_revenue, rev_to_make_and_made
from tasks.expected_customer_behavior_2 import ExpectedCustomerBehavior


def test_last_transaction_dates(transactions, last_transaction_date):
    transactions = transactions
    last_transaction_date = last_transaction_date
    cust_ids = transactions.index.unique()
    for cust_id in cust_ids:
        cust_transactions = transactions.loc[cust_id]
        expected_behavior = ExpectedCustomerBehavior(transactions=cust_transactions,
                                                     last_date=dt.date(2021, 7, 16))
        assert (
            str(expected_behavior.last_transaction_date) ==
            str(last_transaction_date.loc[cust_id].last_transaction_date)
        ), (
            "The last transaction dates don't match; "
            f"cust_id: {cust_id}; "
            f"{str(expected_behavior.last_transaction_date)} == "
            f"{str(last_transaction_date.loc[cust_id].last_transaction_date)}"
        )


def test_expected_rev(transactions, expected_revenue):
    transactions = transactions
    expected_revenue = expected_revenue
    cust_ids = transactions.index.unique()
    for cust_id in cust_ids:
        cust_transactions = transactions.loc[cust_id]
        expected_behavior = ExpectedCustomerBehavior(transactions=cust_transactions,
                                                     last_date=dt.date(2021, 7, 16))
        res = expected_behavior.expected_daily_rev
        answer = expected_revenue.loc[cust_id].exp_rev_med

        assert (
            1 + res == pytest.approx(answer + 1, .15)
        ), (
            "The Expected daily revenue doesn't match; "
            f"cust_id: {cust_id}; "
            f"{floor(expected_behavior.expected_daily_rev)} == "
            f"{floor(expected_revenue.loc[cust_id].exp_rev_med)}"
        )


def test_rev_to_make(transactions, rev_to_make_and_made):
    transactions = transactions
    rev_to_make_and_made = rev_to_make_and_made
    cust_ids = transactions.index.unique()
    for cust_id in cust_ids:
        cust_transactions = transactions.loc[cust_id]
        expected_behavior = ExpectedCustomerBehavior(transactions=cust_transactions,
                                                     last_date=dt.date(2021, 7, 16))
        res = expected_behavior.expected_rev_until_last_date
        answer = rev_to_make_and_made.loc[cust_id].rev_to_make
        assert (
            1 + res == pytest.approx(answer + 1, .15)
        ), (
            "The Expected daily revenue doesn't match; "
            f"cust_id: {cust_id}; "
            f"{floor(expected_behavior.expected_rev_until_last_date)} == "
            f"{floor(rev_to_make_and_made.loc[cust_id].rev_to_make)}"
        )


def test_rev_made(transactions, rev_to_make_and_made):
    transactions = transactions
    rev_to_make_and_made = rev_to_make_and_made
    cust_ids = transactions.index.unique()
    for cust_id in cust_ids:
        cust_transactions = transactions.loc[cust_id]
        expected_behavior = ExpectedCustomerBehavior(transactions=cust_transactions,
                                                     last_date=dt.date(2021, 7, 16))
        res = expected_behavior.rev_made
        answer = rev_to_make_and_made.loc[cust_id].rev_made
        print(cust_id, res, answer)
        assert (
            1 + res == pytest.approx(answer + 1, .15)
        ), (
            "The Expected daily revenue doesn't match; "
            f"cust_id: {cust_id}; "
            f"{floor(expected_behavior.rev_made)} == "
            f"{floor(rev_to_make_and_made.loc[cust_id].rev_made)}"
        )