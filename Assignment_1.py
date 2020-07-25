'''
# Assignment 1
# Drawing Graphs in python 3.6
'''

import numpy as np
import matplotlib.pyplot as plt
import json
from datetime import date, datetime, timedelta
import matplotlib
matplotlib.use("TkAgg")
matplotlib.style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

global data
with open("data.json") as f:
		data = json.load(f)

cur = [c for c in data['rates']['2019-01-02']]
cur.append('')
cur.sort()

def update_graph():

	start_date=date(2019,1,1)
	end_date=date(2019,1,31)
	
	# print(dates)
	c1=cur1.current()
	c2=cur2.current()
	print(c1,c2)
	
	if(c1<=0 and c2<=0): 
		return
	if(c1>0 and c2>0): 
		t=cur[c1]+ ' and ' +cur[c2]
	else: 
		if c1<=0: 
			t=cur[c2]
		else:
			t=cur[c1]
	title = t+" exchange rate against EUR from 1 Jan to 31 Jan 2019"


	dates = [start_date + timedelta(days=x) for x in range((end_date-start_date).days + 1)]
	dates = [x.strftime("%Y-%m-%d") for x in dates]

	INR=[]
	GBP=[]

	weekend=[]

	for d in dates:
		try:
			if c1>0: 
				INR.append(data['rates'][d][cur[c1]])
			if c2>0: 
				GBP.append(data['rates'][d][cur[c2]])
		except KeyError:
			weekend.append(d)

	dates = list(set(dates) - set(weekend))
	dates.sort()

	INR = np.array(INR, dtype=float)
	GBP = np.array(GBP, dtype=float)


	# df=pd.DataFrame({'Dates':dates,'GBP':GBP})
	# print(df)

	axes.clear()
	axes.plot(dates,INR,"#00A3E0",  linestyle = 'solid')
	if c2>0: 
		axes.plot(dates,GBP, linestyle = 'solid', color='r')


	# axes.grid(axis='y' , linestyle='-', linewidth=0.5)
	axes.set_xlabel("TIME", labelpad=10.2)
	axes.set_ylabel("Rates against EUR", labelpad=10.2)
	axes.set_title(title)


	d=int(len(dates)/12) + 1
	ticks=[i for i in range(0,len(dates),d)]
	xlab = [d[-2:]+d[4:7] for d in dates]
	
	axes.set_xticks(ticks)
	axes.set_xticklabels(xlab[::d])
	canvas.draw()

	# print(dates)
	# multi = MultiCursor(fig.canvas, axes, color='r', lw=1,horizOn=True, vertOn=True)
	


app = tk.Tk()
app.title("Graph")
L1 = tk.Label(app, text="")
L1.pack(pady=20,side=tk.TOP, fill=tk.BOTH, expand=False)

f = Figure(figsize=(9,5), dpi=100)
axes = f.add_subplot(111)


button = ttk.Button(app, text="Update", command=update_graph)
button.place(x=800,y=10)

basecur = ttk.Combobox(app, state="readonly")
basecur.place(x=100,y=10)
cur1 = ttk.Combobox(app, values=cur, state="readonly")
cur1.place(x=250,y=10)
cur2 = ttk.Combobox(app, values=cur, state="readonly")
cur2.place(x=250,y=40)
basecur.set("EUR")

global canvas
canvas = FigureCanvasTkAgg(f, master= app)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

toolbar = NavigationToolbar2Tk( canvas, window= app)
toolbar.update()
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app.mainloop()

