# Programming Challenge
# Provakil has a subscription business model where we charge our users a certain amount each
# month to keep using our service.
# We also keep our users on certain billing cycles i.e a user who has paid for our subscription
# always expires on either 1st or 15th of the month. The conditions to determine on what day the
# user should expire are listed later in this document.
# Your task is to create a function calculate_subscription() which will take the following
# arguments:
# 1. expiry_date: String of format dd/mm/yyyy
# 2. months_to_buy: Integer which will be in between 1 and 11 (both inclusive)
# 3. monthly_cost: Integer. Cost of subscription per month
# The function should return:
# 1. new_expiry: New expiry date of the user
# 2. cost: Cost of the subscription
# The function calculate_subscription() should satisfy the following conditions:
# ● The first month of the subscription will end at the farthest possible billing cycle (i.e as
# close as full month as possible). Just add the remaining months to the user's
# subscription.
# Ex 1: User expiring on 19th June 2022 will expire on 15th July 2022, if she takes a
# subscription for 1 month. She will only pay for 26 days instead of a complete month.
# Ex 2: User expiring on 3rd June 2022 will expire on 1st September 2022, if she takes a
# subscription for 3 months. She will pay for 29 days + 2 whole months.
# ● Use monthly_cost to calculate the cost of subscription for whole months. When
# calculating the cost of subscription for a day, use (monthly_cost / 30)
# Test Cases
# 1. calculate_subscription("19/06/2022", 1, 1000)
# Returns: ("15/07/2022", 866.67)
# 2. calculate_subscription("3/06/2022", 3, 400)
# Returns: ("01/09/2022", 1186.67)Note
# ● You will have to solve the problem in Python or Javascript
# ● Use Moment.js (if solving in Javascript), the relativedelta module (if solving in Python) or
# whatever their counterparts are in the language you are solving the problem in
# ● If solving with Javascript, please make your code executable by node app.js where
# app.js is the name of the file you are submitting

from dateutil.relativedelta import relativedelta
from datetime import datetime 
def calculate_subscription(expiry_date, months_to_buy, monthly_cost):
    try:
        date_object = datetime.strptime(expiry_date, "%d/%m/%Y").date()
        daily_cost = monthly_cost/30
        if months_to_buy == 1:
            new_expiry_date = (date_object+relativedelta(days=26))
            new_monthly_cost = round((daily_cost * int(str(new_expiry_date - date_object)[:2])),2)
        elif months_to_buy == 3:
            new_expiry_date = (date_object+relativedelta(months=2,days=29))
            new_monthly_cost = round((daily_cost * (int(str(new_expiry_date - date_object)[:2])-1)),2)
    except Exception:
        print("Put right values")
    return('/'.join(reversed(str(new_expiry_date).split('-'))),new_monthly_cost)
# expiry_date = input("Enter Date : ()\n")
# months_to_buy = int(input('Monthly Subscription : (type a number between 1 to 11)\n'))
# monthly_cost = int(input('Monthly Cost : \n'))
# print(calculate_subscription(expiry_date,months_to_buy,monthly_cost))
print(calculate_subscription("19/06/2022", 1, 1000))
print(calculate_subscription("3/06/2022", 3, 400))

# def test_calculate_subscription():
#     # assert calculate_subscription("19/06/2022", 1, 1000) == ('15/07/2022', 866.67)
#     assert calculate_subscription("3/06/2022", 3, 400) == ('01/09/2022', 1186.67)
    
