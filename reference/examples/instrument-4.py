from neutronpy.resolution import Instrument
from numpy import linspace

EXP = Instrument()
EXP.plot_projections([1., 1., 0., linspace(0, 15, 7)])