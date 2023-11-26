import pygmt
import numpy as np

# Coordinates for Sonthofen
latitude = 47.51
longitude = 10.28

# Approximate conversion from degrees to kilometers
km_per_degree_latitude = 111
km_per_degree_longitude = 111 * np.cos(np.radians(latitude))

# Calculate the change in latitude and longitude for 5 km
delta_latitude = 10 / km_per_degree_latitude
delta_longitude = 10 / km_per_degree_longitude

# Create the region
region = [longitude - delta_longitude, longitude + delta_longitude, latitude - delta_latitude, latitude + delta_latitude]

# Load sample earth relief data
grid = pygmt.datasets.load_earth_relief(resolution="01s", region=[longitude - delta_longitude, longitude + delta_longitude, latitude - delta_latitude, latitude + delta_latitude]) #region=[10.25, 10.35, 47.45, 47.55]) #region=[-92.5, -82.5, -3, 7])

fig = pygmt.Figure()
fig.grdcontour(
    # annotation=250,
    interval=50,
    grid=grid,
    projection="M10c",
)
fig.show()

