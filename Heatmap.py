import plotly.graph_objects as go

import numpy as np

 

import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0, 10, 50)
y = np.linspace(0, 10, 40)
x,y = np.meshgrid(x,y)
z = (np.sin(x+y)*3 + np.cos(y+5))

plt.contourf(x, y, z, cmap = 'Reds')
plt.colorbar()

plt.show()

fig = go.Figure(data =
    go.Contour(
        
z =   (np.sin(x+y)*3 + np.cos(y+5)),
        dx=10,
        x0=5,
        dy=10,
        y0=10,
        line_smoothing=0.95
    )
)

fig.show()