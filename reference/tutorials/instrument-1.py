from matplotlib import pyplot as plt
from numpy import rad2deg, arctan

fig = plt.figure(facecolor='w', edgecolor='k', figsize=(8, 2))
axis = plt.Axes(fig, [0., 0., 1., 1.])
axis.set_axis_off()
fig.add_axes(axis)
plt.subplots_adjust(0, 0, 1, 1, 0, 0)

guide = plt.Rectangle((-4, 1), 0.5, 0.25, fc='g', zorder=2)
guide_mono = plt.Line2D((-4, -2), (1.125, 1.125), lw=1, ls='-.', zorder=1)
axis.text(-4, 0.75, 'Guide')
axis.text(-3, 1.25, 'Col$_{1}$', size=10)

mono = plt.Rectangle((-2, 1 - 0.125), 0.05, 0.5, fc='b', zorder=2)
mono_samp = plt.Line2D((-2, 0), (1.125, 0), lw=1, ls='-.', zorder=1)
axis.text(-2.75, 0.5, 'Monochromator')
axis.text(-1, 0.75, 'Col$_{2}$', size=10)

sample = plt.Circle((0, 0), radius=0.125, fc='y', zorder=2)
samp_ana = plt.Line2D((0, 2), (0, 1.125), lw=1, ls='-.', zorder=1)
axis.text(-0.35, 0.35, 'Sample')
axis.text(0.8, 0.75, 'Col$_{3}$', size=10)

analyzer = plt.Rectangle((2 - 0.2, 1 + 0.2), 0.5, 0.05, fc='b', zorder=2, angle=-10)
ana_det = plt.Line2D((2, 4), (1.125, 0), lw=1, ls='-.', zorder=1)
axis.text(1.6, 0.55, 'Analyzer')
axis.text(3., 0.75, 'Col$_{4}$', size=10)

detector = plt.Rectangle((4, 0 - 0.125), 0.5, 0.25, fc='r', angle=rad2deg(arctan(-1.125 / 2.)), zorder=2)
axis.text(3.8, 0.325, 'Detector')

for item in [guide_mono, mono_samp, samp_ana, ana_det]:
    fig.gca().add_line(item)

for item in [guide, mono, sample, analyzer, detector]:
    fig.gca().add_patch(item)

axis.axis('scaled')
axis.axis('off')

plt.show()