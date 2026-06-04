python-data-viz :

Learning matplotlib from scratch — every major chart type covered with real examples. This was the foundation before moving into seaborn and eventually building real financial dashboards.

What's covered :

> Line plots with multiple series
> Customizing plots — markers, colors, line styles, font sizes
> Bar charts — vertical and horizontal
> Histograms — distribution of data with bins
> Pie charts — with explode, shadow, percentage labels
> Scatter plots — correlation between two variables with multiple classes
> Subplots — 2x2 grid layout on one figure
>Grid lines — making plots easier to read
> Labels and titles — fonts, colors, weights, tick params
> pandas + matplotlib — plotting directly from a CSV file


Files
File                                  What it does
getting_started.py	           First line plot — simple x/y with numpy arrays
customizing_plot.py            Multi-line plot with custom markers, colors, line styles
lables.py	                     Titles, axis labels, fonts, colors, tick parameters
grid_lines.py               	 Adding reference grid lines to plots
barchart.py	                   Vertical bar chart — food consumption by category
Histogram.py                 	 Exam score distribution with normal distribution data
piechart.py	                   Student year breakdown with explode and shadow
scatter_graph.py	             Study hours vs test scores — two classes compared
subplots.py	                   2x2 subplot grid — linear, quadratic, cubic, quartic
mat+pandas.py	               Reading a CSV with pandas and plotting directly

Stack :
Python, matplotlib, numpy, pandas

Setup :
bashgit clone https://github.com/prince-gupta79/python-data-viz.git
cd python-data-viz
pip install matplotlib numpy pandas
Run any file:
bashpython getting_started.py

Why I built this :
Before building the market intelligence system with real financial charts, I needed to understand matplotlib properly. This folder is where I learned every chart type from scratch — how to control colors, fonts, markers, layouts, and how to go from raw data to a readable visualization.
The subplots file was particularly useful — understanding how to arrange multiple plots on one canvas is something that shows up constantly in real data science work.

Built in Nepal. Part of a self-directed journey into ML and data science
