from bokeh.models import LinearColorMapper, ColorBar
from bokeh.transform import transform
from bokeh.plotting import figure,show
import pandas as pd
 
# Creating a set of data in d
d={'Col0':[ 190, 320, 270, 874, 459, 124, 546,
           285, 341, 980, 1002, 453, 324, 245],
   'Col1':[ 71, 128, 34, 49, 52, 87, 78, 25, 67,
           19, 34, 100, 287, 55],
   'Col2':[ 1123, 6471, 8345, 3253, 6420, 1830,
           7849, 2937, 2108, 5392, 1273, 3928, 4927, 7392]}
 
# Set of data into a dataframe 
 
df = pd.DataFrame(d)
 
# Color bar template and minimum and maximum values
color = LinearColorMapper(palette = 'Turbo256', low = df.Col0.min(), high = df.Col0.max())
 
# Figure with specified axes 
colorbar = figure(plot_width = 750, plot_height = 600, x_axis_label = 'Column 1', y_axis_label = 'Column 2')
 
# Plotting the points with defined size and opacity
colorbar.circle(x = 'Col1', y = 'Col2', source = df, color = transform('Col0', color), size = 15, alpha = 0.5)
 
# Location in the plot
color_bar = ColorBar(color_mapper = color, label_standoff = 14, location = (0,0), title = 'Plot')
 
# Defining the position of the color bar
colorbar.add_layout(color_bar, 'right')
 
# Showing the above implementation
show(colorbar)