import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from neutronpy import Instrument, Sample
from neutronpy.functions import resolution

EXP = Instrument()

hkle = [1., 1., 0., 5.]
EXP.calc_projections(hkle)

x, y = np.meshgrid(np.linspace(-0.05, 0.05, 101), np.linspace(-0.05, 0.05, 101), sparse=True)

R0, RMxx, RMyy, RMxy = EXP.get_resolution_params(hkle, 'QxQy', mode='project')
p = np.array([0., 0., 1., 0, 0, R0, RMxx, RMyy, RMxy])
z = resolution(p, (x, y))

fig = plt.figure(facecolor='w', edgecolor='k')

plt.pcolormesh(x, y, z, cmap=cm.jet)

[x1, y1] = EXP.projections['QxQy'][0]
plt.fill(x1, y1, 'r', alpha=0.25)
[x1, y1] = EXP.projections['QxQySlice'][0]
plt.plot(x1, y1, 'w--')

plt.xlim(-0.05, 0.05)
plt.ylim(-0.05, 0.05)

plt.show()