"""
Creating a map with contour lines
=================================

Plotting a contour map is handled by :meth:`pygmt.Figure.grdcontour`.

.. note::

    This tutorial assumes the use of a Python notebook, such as IPython or Jupyter Notebook.
    To see the figures while using a Python script instead, use
    ``fig.show(method="external)`` to display the figure in the default PDF viewer.

    To save the figure, use ``fig.savefig("figname.pdf")`` where ``"figname.pdf"``
    is the desired name and file extension for the saved figure.
"""
# sphinx_gallery_thumbnail_number = 5

import pygmt
import numpy as np

# Coordinates for Nürnberg
latitude = 49.45
longitude = 11.07

# Approximate conversion from degrees to kilometers
km_per_degree_latitude = 111
km_per_degree_longitude = 111 * np.cos(np.radians(latitude))

# Calculate the change in latitude and longitude for 5 km
delta_latitude = 25 / km_per_degree_latitude
delta_longitude = 25 / km_per_degree_longitude

# Create the region
region = [longitude - delta_longitude, longitude + delta_longitude, latitude - delta_latitude, latitude + delta_latitude]

# Load sample earth relief data
grid = pygmt.datasets.load_earth_relief(resolution="01s", region=[longitude - delta_longitude, longitude + delta_longitude, latitude - delta_latitude, latitude + delta_latitude]) #region=[10.25, 10.35, 47.45, 47.55]) #region=[-92.5, -82.5, -3, 7])

########################################################################################
# Create contour plot
# -------------------
#
# The :meth:`pygmt.Figure.grdcontour` method takes the grid input.
# It plots annotated contour lines, which are thicker and have the
# elevation/depth written on them, and unannotated contour lines.
# In the example below, the default contour line intervals are 500 meters,
# with an annotated contour line every 1000 meters.
# By default, it plots the map with the
# equidistant cylindrical projection and with no frame.

# fig = pygmt.Figure()
# fig.grdcontour(grid=grid)
# fig.show()

########################################################################################
# Contour line settings
# ---------------------
#
# Use the ``annotation`` and ``interval`` arguments to adjust contour line intervals.
# In the example below, there are contour intervals every 250 meters and
# annotated contour lines every 1,000 meters.

fig = pygmt.Figure()
fig.grdcontour(
    annotation=250,
    interval=20,
    grid=grid,
    projection="M10c",
)
fig.text(
    x=longitude,
    y=latitude,
    text="Nürnberg",
    font="8p,Helvetica-Bold,black",
    justify="CM",
)
fig.show()

########################################################################################
# Contour limits
# --------------
#
# The ``limit`` argument sets the minimum and maximum values for the contour lines.
# The argument takes the low and high values,
# and is either a list (as below) or a string ``limit="-4000/-2000"``.

fig = pygmt.Figure()
fig.grdcontour(
    annotation=250,
    interval=20,
    grid=grid,
    # limit=[-4000, -2000],
)
fig.show()

########################################################################################
# Map settings
# ------------
#
# The :meth:`pygmt.Figure.grdcontour` method accepts additional arguments,
# including setting the projection and frame.

fig = pygmt.Figure()
fig.grdcontour(
    annotation=250,
    interval=20,
    grid=grid,
    # limit=[-4000, -2000],
    projection="M10c",
    frame=True,
)
fig.show()

########################################################################################
# Adding a colormap
# -----------------
#
# The :meth:`pygmt.Figure.grdimage` method can be used to add a
# colormap to the contour map. It must be called prior to
# :meth:`pygmt.Figure.grdcontour` to keep the contour lines visible on the final map.
# If the ``projection`` argument is specified in the :meth:`pygmt.Figure.grdimage`
# method, it does not need to be repeated in the :meth:`pygmt.Figure.grdcontour` method.

fig = pygmt.Figure()
fig.grdimage(
    grid=grid,
    cmap="haxby",
    projection="M10c",
    frame=True,
)
fig.grdcontour(
    annotation=1000,
    interval=250,
    grid=grid,
    limit=[-4000, -2000],
)
fig.show()
