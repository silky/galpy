from galpy.potential_src import Potential
from galpy.potential_src import MiyamotoNagaiPotential
from galpy.potential_src import LogarithmicHaloPotential
from galpy.potential_src import DoubleExponentialDiskPotential
from galpy.potential_src import PowerSphericalPotential
from galpy.potential_src import TwoPowerSphericalPotential
from galpy.potential_src import plotRotcurve
#
# Functions
#
evaluatePotentials= Potential.evaluatePotentials
evaluateRforces= Potential.evaluateRforces
evaluatezforces= Potential.evaluatezforces
plotPotentials= Potential.plotPotentials
plotRotcurve= plotRotcurve.plotRotcurve

#
# Classes
#
Potential= Potential.Potential
MiyamotoNagaiPotential= MiyamotoNagaiPotential.MiyamotoNagaiPotential
DoubleExponentialDiskPotential= DoubleExponentialDiskPotential.DoubleExponentialDiskPotential
LogarithmicHaloPotential= LogarithmicHaloPotential.LogarithmicHaloPotential
PowerSphericalPotential= PowerSphericalPotential.PowerSphericalPotential
NFWPotential= TwoPowerSphericalPotential.NFWPotential
JaffePotential= TwoPowerSphericalPotential.JaffePotential
HernquistPotential= TwoPowerSphericalPotential.HernquistPotential
TwoPowerSphericalPotential= TwoPowerSphericalPotential.TwoPowerSphericalPotential
