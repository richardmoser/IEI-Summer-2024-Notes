import numpy as np
import math
import ROOT
from ROOT import TF1
from ROOT import TH1F
from ROOT import TCanvas

# Example of a function along the lines of the Maxwell-Boltzmann distribution
# First argument is the variable (or array of variables for N-dim function)
# Second argument is array of parameters
# In this example, we will work with a function with one variable and three parameters
maxwell_boltzmann_npar = 2
def maxwell_boltzmann(var, par):
   # Variable(s)
   v = var[0]
   # Parameters
   A = par[0]
   B = par[1]
   # Computation
   value = A * v**2 * math.exp( - B * v**2 )
   return value

#
# Main program
#

xmin = 0
xmax = 2000
nbins = 50

# Define a ROOT function object using user-defined funtion implementation
# The following function definition works when this script is executed from the command line
# but not when it is executed from Jupyter notebook
#
#func_maxwell_boltzmann = TF1("func_maxwell_boltzmann", maxwell_boltzmann, 
#                             xmin, xmax, maxwell_boltzmann_npar)
#
# An alternative, string definition, of the same function that works both 
# from the command line and when loaded in the Jupyter notebook:
#
func_maxwell_boltzmann = TF1("func_maxwell_boltzmann",
                             "[0] * x * x * exp( -[1] * x * x)",
                             xmin, xmax)

func_maxwell_boltzmann.SetParameters(0.001,5e-6)
# Here, we will normalize the function to make it a true PDF
# Since parameter A (see function definition above) is overall factor, we will adjust it
par0_original = func_maxwell_boltzmann.GetParameter(0)
integral = func_maxwell_boltzmann.Integral(xmin, xmax)
func_maxwell_boltzmann.SetParameter(0, par0_original / integral )

# Next, we will create a histogram and will fill it with random numbers
# that are distributed according to Maxwell-Boltzmann distribution
# representing velocities of atoms in an ideal gas.
n_events = 1000
hist = TH1F("hist","Velocity distribution", nbins, xmin, xmax)
hist.FillRandom("func_maxwell_boltzmann", n_events)
# The above is the easiest method. One can also make a loop over n_events,
# for each event call v=func_maxwell_boltzmann.GetRandom(), and put it into histogram hist.Fill(v)

# Next, draw everything

# Set up canvas
canvas = TCanvas("canvas","My figure", 10,10,1000, 500)
canvas.Draw()
canvas.Divide(2,1)

ROOT.gStyle.SetOptStat(0)   # Switch off plot statistics window

# Draw the first subfigure
canvas.cd(1) 

# Function drawing options
func_maxwell_boltzmann.SetLineColor(ROOT.kBlue)
func_maxwell_boltzmann.SetLineWidth(3)
func_maxwell_boltzmann.SetTitle("Maxwell-Boltzmann distribution function")

func_maxwell_boltzmann.Draw()

# Draw the second subfigure
canvas.cd(2)

# Histogram drawing options
hist.SetLineWidth(2)
hist.SetLineColor(ROOT.kBlue)
hist.GetXaxis().SetTitle("velocity [m/s]")
hist.GetYaxis().SetTitle("number of atoms observed")

hist.Draw("histE")
