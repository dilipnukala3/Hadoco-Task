import datetime as dt
import os

import pandas as pd
import pytest


@pytest.fixture()
def transactions():
    t = pd.read_csv(
        os.path.join(os.getcwd(), 'resources', 'transactions.csv')
    )
    t['transaction_date'] = t['transaction_date'].apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%d").date())
    t.set_index('cust_id', inplace=True)
    return t


@pytest.fixture()
def ipts():
    ipts_ = pd.read_csv(
        os.path.join(os.getcwd(), 'resources', 'test_customer_ipts.csv')
    )
    ipts_.set_index('cust_id', inplace=True)
    return ipts_


@pytest.fixture()
def at_risk_customers():
    arc = pd.read_csv(
        os.path.join(os.getcwd(), 'resources', 'test_at_risk_customers.csv')
    )
    arc.set_index('cust_id', inplace=True)
    return arc


@pytest.fixture()
def expected_revenue():
    er = pd.read_csv(
        os.path.join(os.getcwd(), 'resources', 'test_cust_expected_daily_rev.csv')
    )
    er.set_index('cust_id', inplace=True)
    return er


@pytest.fixture()
def last_transaction_date():
    ltd = pd.read_csv(
        os.path.join(os.getcwd(), 'resources', 'test_last_transaction_dates.csv')
    )
    ltd.set_index('cust_id', inplace=True)
    return ltd


@pytest.fixture()
def rev_to_make_and_made():
    rtm = pd.read_csv(
        os.path.join(os.getcwd(), 'resources', 'test_rev_to_make_and_made.csv')
    )
    rtm.set_index('cust_id', inplace=True)
    return rtm


def test_files(transactions,
               ipts,
               at_risk_customers,
               expected_revenue,
               last_transaction_date,
               rev_to_make_and_made):
    transactions = transactions
    ipts = ipts
    at_risk_customers = at_risk_customers
    expected_revenue = expected_revenue
    last_transaction_date = last_transaction_date
    rev_to_make_and_made = rev_to_make_and_made

    cust_ids_t = set(transactions.index.unique().tolist())
    cust_ids_ipt = set(ipts.index.unique().tolist())
    cust_ids_arc = set(at_risk_customers.index.unique().tolist())
    cust_ids_er = set(expected_revenue.index.unique().tolist())
    cust_ids_ltd = set(last_transaction_date.index.unique().tolist())
    cust_ids_rtm = set(rev_to_make_and_made.index.unique().tolist())
    assert (
        len(cust_ids_t) ==
        len(
            cust_ids_t
            & cust_ids_arc
            & cust_ids_ipt
            & cust_ids_er
            & cust_ids_ltd
            & cust_ids_rtm
        )
    ), "The cust_ids in the files don't match"
