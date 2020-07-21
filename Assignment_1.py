'''
# Assignment 1
# Drawing Graphs in python 3.6
'''

import numpy as np
import matplotlib.pyplot as plt
import json
from datetime import date, datetime, timedelta
import pandas as pd

with open("data.json") as f:
	data = json.load(f)

# all_dates=[]
# for d in data['rates']:
# 	all_dates.append(d)

# all_dates.sort(key=lambda dat: datetime.strptime(dat, "%Y-%m-%d"))
# print(all_dates)

start_date=date(2019,1,1)
end_date=date(2019,1,31)

dates = [start_date + timedelta(days=x) for x in range((end_date-start_date).days + 1)]

dates = [x.strftime("%Y-%m-%d") for x in dates]
# print(dates)

INR=[]
weekend=[]
for d in dates:
	try:
		INR.append(data['rates'][d]['INR'])
	except KeyError:
		weekend.append(d)

dates = list(set(dates) - set(weekend))
print(len(dates),len(INR))

df=pd.DataFrame({'Dates':dates,'INR':INR})
print(df)
plt.plot_date(dates,INR)
plt.show()
