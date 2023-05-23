import json
import eq_explore_data
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Map the earthquakes.
data = [Scattergeo(lon=eq_explore_data.lons, lat=eq_explore_data.lats)]
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')