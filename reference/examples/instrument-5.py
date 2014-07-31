from neutronpy.resolution import Instrument

EXP = Instrument()
EXP.arms = [1560, 600, 260, 300]
EXP.plot_instrument([1,1,0,0])