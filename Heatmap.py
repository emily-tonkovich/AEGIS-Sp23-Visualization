import plotly.graph_objects as go

import numpy as np

fig = go.Figure(data =
    go.Contour(
        
z =   [[2, 4, 7, 12, 13, 14, 15, 16],
       [3, 1, 6, 11, 12, 13, 16, 17],
       [4, 2, 7, 7, 11, 14, 17, 18],
       [5, 3, 8, 8, 13, 15, 18, 19],
       [7, 4, 10, 9, 16, 18, 20, 19],
       [9, 10, 5, 27, 23, 21, 21, 21],
       [11, 14, 17, 26, 25, 24, 23, 22]],
        dx=10,
        x0=5,
        dy=10,
        y0=10,
        line_smoothing=0.95
    )
)

fig.show() 