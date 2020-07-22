'''
# Assignment 1
# Drawing Graphs in python 3.6
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from datetime import date, datetime, timedelta
import pandas as pd
from matplotlib.widgets import MultiCursor

with open("data.json") as f:
	data = json.load(f)


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
dates.sort()
# dates = pd.to_datetime(dates)
# print(dates)
INR = np.array(INR, dtype=float)

df=pd.DataFrame({'Dates':dates,'INR':INR})
print(df)

fig, axes = plt.subplots()
axes.plot(dates,INR, linestyle = 'solid')
plt.ylim(np.round(np.min(INR)), np.round(np.max(INR)))

plt.xticks([0,len(dates)], [dates[0],dates[-1]])
plt.grid(axis='y' , linestyle='-', linewidth=0.5)

# print(dates)
# multi = MultiCursor(fig.canvas, axes, color='r', lw=1,horizOn=True, vertOn=True)

plt.show()
