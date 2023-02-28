#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#  PROVAKIL Assignment


# In[15]:


from datetime import datetime
from dateutil.relativedelta import relativedelta
def calculate_subscription(expiry_date,months_to_buy,monthly_cost):

    ed_datetime=datetime.strptime(expiry_date,'%d/%m/%Y')

    subp=ed_datetime + relativedelta(months=+months_to_buy)

    if subp.day>15:
        subp=subp.replace(day=15)
    else:
        subp=subp.replace(day=1)

    no_of_days=(subp-ed_datetime).days
    perday=monthly_cost/30
    new_expiry = subp.strftime("%d/%m/%Y")
    numofmonths=(subp.year - ed_datetime.year) * 12 + subp.month - ed_datetime.month -1
  
    l=[]
    for i in range(ed_datetime.month,subp.month-1):
        if((i==2) and ((subp.year%4==0)  or ((subp.year%100==0) and (subp.year%400==0)))) :
            l.append(29)

        elif(i==2) :
            l.append(28)

        elif(i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12) :
            l.append(31)

        else :
            l.append(30)

    daysinm=sum(l)
    remdays=no_of_days-daysinm
    cost=numofmonths*monthly_cost +(perday*remdays)
   
    return(new_expiry,cost)


print(calculate_subscription("19/06/2022", 1, 1000))
print(calculate_subscription("3/06/2022", 3, 400))


# In[ ]:




