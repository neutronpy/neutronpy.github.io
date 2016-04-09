from neutronpy import Material
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
h, k = np.meshgrid(np.linspace(0, 2, 81), np.linspace(0, 2, 81))
def_FeTe = {'name': 'Fe1.1Te',
            'composition': [{'ion': 'Fe', 'pos': [0.75, 0.25, 0.0]},
                            {'ion': 'Fe', 'pos': [0.25, 0.75, 0.0]},
                            {'ion': 'Te', 'pos': [0.25, 0.25, 0.2839]},
                            {'ion': 'Te', 'pos': [0.75, 0.75, -0.2839]},
                            {'ion': 'Fe', 'pos': [0.25, 0.25, 0.721], 'occupancy': 0.1},
                            {'ion': 'Fe', 'pos': [0.75, 0.75, -0.721], 'occupancy': 0.1}],
            'debye-waller': False,
            'massNorm': True,
            'lattice': {'abc': [3.81, 3.81, 6.25],
                        'abg': [90, 90, 90]}}
FeTe = Material(def_FeTe)
str_fac = 0.25 * (np.abs(FeTe.calc_nuc_str_fac((h, k, 0))) ** 2 +
                  np.abs(FeTe.calc_nuc_str_fac((-h, k, 0))) ** 2 +
                  np.abs(FeTe.calc_nuc_str_fac((h, -k, 0))) ** 2 +
                  np.abs(FeTe.calc_nuc_str_fac((-h, -k, 0))) ** 2)
plt.pcolormesh(h, k, str_fac, cmap=cm.jet)
plt.xlabel('h (r.l.u.)')
plt.ylabel('k (r.l.u.)')
plt.show()