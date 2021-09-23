import os
import sys
import datetime as dt
from math import floor

import pytest
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tests.test_initial import transactions, at_risk_customers
from tasks.customer_3 import Customer


@pytest.fixture()
def correct_answers(transactions, at_risk_customers):
    transactions = transactions
    at_risk_customers = at_risk_customers
    cust_ids = transactions.index.unique()

    correct = 0
    for cust_id in cust_ids:
        cust_transactions = transactions.loc[cust_id]
        cust = Customer(transactions=cust_transactions,
                        last_date=dt.date(2021, 7, 16))

        res = int(cust.at_risk)
        answer = int(at_risk_customers.loc[cust_id].at_risk)
        if res == answer:
            correct += 1
    return correct


def test_above_20_perc(correct_answers, transactions):
    correct_answers = correct_answers
    transactions = transactions

    n_customers = transactions.index.unique().shape[0]
    assert correct_answers / n_customers > .2, (
        "The Correct answers are below 20%; "
    )


def test_above_40_perc(correct_answers, transactions):
    correct_answers = correct_answers
    transactions = transactions

    n_customers = transactions.index.unique().shape[0]
    assert correct_answers / n_customers > .4, (
        "The Correct answers are below 40%; "
    )


def test_above_60_perc(correct_answers, transactions):
    correct_answers = correct_answers
    transactions = transactions

    n_customers = transactions.index.unique().shape[0]
    assert correct_answers / n_customers > .6, (
        "The Correct answers are below 60%; "
    )


def test_above_80_perc(correct_answers, transactions):
    correct_answers = correct_answers
    transactions = transactions

    n_customers = transactions.index.unique().shape[0]
    assert correct_answers / n_customers > .8, (
        "The Correct answers are below 80%; "
    )