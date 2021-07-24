# line_chart_with_default_settings.py

# import the required library
import matplotlib.pyplot as plt

# X and Y data
numberofemp = [13, 200, 250, 300, 350, 400]
year = [2011, 2012, 2013, 2014, 2015, 2016]

# plot a line chart
plt.plot(year, numberofemp)
plt.show()