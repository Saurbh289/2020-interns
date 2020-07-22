'''
# Assignment 1
# Drawing Graphs in python 3.6
'''

import numpy as np
import matplotlib.pyplot as plt
import json
from datetime import date, datetime, timedelta
# import pandas as pd


with open("data.json") as f:
	data = json.load(f)


start_date=date(2019,1,1)
end_date=date(2019,1,31)


dates = [start_date + timedelta(days=x) for x in range((end_date-start_date).days + 1)]
dates = [x.strftime("%Y-%m-%d") for x in dates]

# print(dates)


INR=[]
GBP=[]

weekend=[]

for d in dates:
	try:
		INR.append(data['rates'][d]['INR'])
		GBP.append(data['rates'][d]['GBP'])
	except KeyError:
		weekend.append(d)

dates = list(set(dates) - set(weekend))
dates.sort()

INR = np.array(INR, dtype=float)
GBP = np.array(GBP, dtype=float)


# df=pd.DataFrame({'Dates':dates,'GBP':GBP})
# print(df)

fig, axes = plt.subplots()
plt.plot(dates,INR, linestyle = 'solid')
plt.plot(dates,GBP, linestyle = 'solid', color='r')

# plt.ylim(np.round(np.min(INR)), np.round(np.max(INR)))

plt.xticks([0,len(dates)], [dates[0],dates[-1]])
plt.grid(axis='y' , linestyle='-', linewidth=0.5)
plt.xlabel("TIME")
plt.ylabel("Rates against EUR")
plt.title("INR and GBP exchange rate against EUR from 1 Jan to 31 Jan 2019")

# print(dates)
# multi = MultiCursor(fig.canvas, axes, color='r', lw=1,horizOn=True, vertOn=True)

plt.show()
