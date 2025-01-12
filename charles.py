import numpy as np
import pandas as pd
import chardet
import plotly.express as px
import scipy.stats as ss

def count(E):
	count = {}
	for e in E:
		count[e] = 0
	for e in E:
		count[e] += 1
	print(count)
	return count
	
	
def get_best_distribution(data):
    dist_names = ["norm", "exponweib", "weibull_max", "weibull_min", "pareto", "genextreme"]
    dist_results = []
    params = {}
    for dist_name in dist_names:
        dist = getattr(ss, dist_name)
        param = dist.fit(data)

        params[dist_name] = param
        # Applying the Kolmogorov-Smirnov test
        D, p = ss.kstest(data, dist_name, args=param)
        print("p value for "+dist_name+" = "+str(p))
        dist_results.append((dist_name, p))

    # select the best fitted distribution
    best_dist, best_p = (max(dist_results, key=lambda item: item[1]))
    # store the name of the best fit and its p value

    print("Best fitting distribution: "+str(best_dist))
    print("Best p value: "+ str(best_p))
    print("Parameters for the best fit: "+ str(params[best_dist]))

    return best_dist, best_p, params[best_dist]
  
def Charles():
#	dates = pd.date_range("20250101", periods=12)
#	print(dates)
#	x = open('2024.csv', 'rb')
#	for line in x.readlines():
#		result = chardet.detect(line)
#		print(result)
	x = pd.read_csv('2024.CSV', encoding='ascii')
#	print(x)
#	x = x.head()

#	x = x.drop(columns=['Product code', 'Bureau of Meteorology station number'])
# Product code,Bureau of Meteorology station number,Year,Month,Day,Rainfall amount (millimetres),Period over which rainfall was measured (days),Quality
#	print(x.describe())
#	print(x.info())
	x.set_axis(axis=1, labels=['Product code', 'Bureau of Meteorology station number', "Year" ,"Month","Day","Rainfall amount (millimetres)","Period over which rainfall was measured (days)","Quality"])
#	print(x)
	months = {}
	for n in range(1, 12 + 1):
		months[n] = []
		
	for n in range(1, 12 + 1):
		temp = x.loc[(x['Year'] == 2024) & (x['Month'] == n)]
#		print(x.loc[(x['Year'] == 2024) & (x['Month'] == n)])
		months[n] = list(temp["Rainfall amount (millimetres)"])
#		print(temp['Day'], temp['Rainfall amount (millimetres)'])
	import matplotlib.pyplot as plt
	mons  = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	col = ["crimson", "mediumvioletred", "blue", "orange", "green", "purple", "pink", "grey", "olive", "darkkhaki", "lightsalmon", "sierra"]
	plt.figure(0, dpi=120, figsize=[10, 5])
	all = []
	c = 1
	for m in months:
		d = 1
		day = []
		rain = []
		for r in months[m]:
			day.append(d)
			d += 1
			rain.append(r)
			all.append(r)
		df = pd.DataFrame([{"Day": day, "Rain": rain}])
		df.fillna(0, inplace=True)
#		print(df)
#	exit(1)
#		df.to_csv("{}.csv".format(mons[c - 1]))
#		fig = px.line(df, x=day, y=rain, title="{} 2024 Rainfall Byron Bay".format(mons[c - 1]))
#		fig.write_html("2024-{}-Rainfall_ctruscott.html".format(mons[c - 1]))
#		exit(1)
#	plt.hist(all)
#	plt.show()
	print(all)
	import math
	import statistics
	from scipy.stats import geom
	all = [e for e in all if not math.isnan(e)]
	print(all)
	print("Mean Rainfall 2024 ", statistics.mean(all))
	print("Variance Rainfall 2024 ", statistics.variance(all))
	print("Standard Deviation ", statistics.stdev(all))
	
#		plt.title("Charles Truscott Watters. Byron Bay Rainfall# 2024".format(m))
#		plt.plot(day, rain, label="{} Rainfall in mm".format(mons[c - 1]))
#		plt.xlabel("Day")
#		plt.ylabel("mm rain")
#		plt.legend()
#	#	plt.savefig('{}.png'.format(c))
#		c += 1
#		print(day, rain)
#	plt.hist(all, density=True)
#	plt.show()
#	ss.mode(all)
	count = len(all)
	d = np.histogram(all)
	print(d[0])
	d1 = d[0]
	d2 = d[1]
#	count = len(d[0])
	for x, y in zip(d1, d2):
		print("Frequency: {}, Rainfall:{}, Rel Freq: {}".format(x, y, x / count * 100))

#	dist = ss.pareto.rvs(5.667441860465116, 13.547087920669176,  365)
#	plt.hist(dist, cumulative=True, edgecolor='black', linewidth=0.5)
#	plt.scatter(np.arange(365), dist)
#	plt.hist(dist)
#	plt.show()
"""	Frequency: 1, Rainfall:97.74, Rel Freq: 0.29069767441860467
p value for norm = 1.573103218921803e-35
p value for exponweib = 4.2821880379098994e-85
p value for weibull_max = 5.6987276913223715e-286
p value for weibull_min = 4.338292107531359e-85
p value for pareto = 9.242748581805762e-95
p value for genextreme = 3.446323895106048e-75
Best fitting distribution: norm
Best p value: 1.573103218921803e-35
Parameters for the best fit: (5.667441860465116, 13.547087920669176)
"""

#	print(dist)
#	counted = count(all)

#		fig = px.scatter(df, x="Day", y="Rain", title="Byron Rainfall 2024")
#		fig.show()
#		exit(1)
#	get_best_distribution(all)
		
#	for m in months:
#		print(months[m])
#		for d in m:
			
#	print(x.info())
#	print(x.describe())
if __name__ == """__main__""": Charles()