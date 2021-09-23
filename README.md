# Tasks
 
1. Customer Info
 - Calculate the median `ipt` (interpurchase time) for the customer. 
 The IPT is defined as the time between purchases.

2. Expected Customer Behavior
 - calculate the `last_transaction_date`, 
 until which the data should be used for the calculation of the expected behavior.
 To do that you have to:
    1. Create the `ipt_product` by multiplying the `ipt` from 1) with `IPT_FACTOR`
    2. Slice the transactions from `self.last_date - ipt_product * 2` until `self.last_date - ipt_product`
    3. Select the transaction date which has the **highest** revenue. 
    If there are no transactions in the slice, select the last possible date before `self.last_date - ipt_product`.
    
 - Calculate the Expected **daily** revenue by
    1. <u>Option 1</u>: Slicing the transactions until the `last_transaction_date`, calculating the revenue per day 
    and getting the median from it
    2. <u>Option 2 (Bonus)</u>: Fitting a Probability Distribution and getting the .5 quantile.
 
 - Calculate the expected revenue until the `last_date` by multiplying the expected daily revenue
  by the remaining days (from `last_transaction_date` until `last_date`)
  
 - Calculate the `rev_made` (the revenue that was really made) **after** the `last_transaction_date`
 
3. Customer
 - Here is the part where you can calculate if the customer is at risk or not. To do that 
  you have to calculate the quotient between the `revenue_made` (From 2) and the `expected_rev` (From 2)
. For the definition of a customer at risk, please use the `AtRisk` class. It is there to make sure 
that there are no unclarities to spelling and mapping.

For the classification of a customer at risk, try to achieve values > 60%, ideally > 80%.

---

###  NB:
 1. The transaction data is in `resources/transactions.csv`
 2. All tasks are defined for a single customer 
 3. You can test your solutions with pytest. Every file has a corresponding test.
 4. The `last_date` is a date that is always provided as an external parameter. The last_date here is the 16.07.2021 (this is also in the tests) 
  
E.g.
```
# For all tests:
pytest

# For a single module
pytest tests/test_customer_info.py
```

If you have any import errors - Add the project directory to the PYTHONPATH
When you are in the project directory run the following command:
```
# Linux: 
export PYTHONPATH=$PWD
echo $PYTHONPATH

Command Prompt: 
set PYTHONPATH=%cd%
echo %PYTHONPATH%

Powershell: 
$env:PYTHONPATH=$(Get-Location)
echo $Env:PYTHONPATH
```

---

# Customer AT risk:

![](Customer%20AT%20risk.PNG)

---

# Customer NOT at risk:

![](Customer%20NOT%20at%20risk.PNG)
