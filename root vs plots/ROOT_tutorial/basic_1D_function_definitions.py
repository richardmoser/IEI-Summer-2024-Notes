import numpy as np
import math
import ROOT
from ROOT import TF1
from ROOT import TH2F
from ROOT import TCanvas

# Example of a user-defined function.
# First argument is the variable (or array of variables for N-dim function)
# Second argument is array of parameters

# In this example, we will work with one variable and three parameters
myfunc1D_npar = 3
def myfunc1D(var, par):
   # Variable(s)
   x = var[0]
   # Parameters
   A = par[0]
   B = par[1]
   tau = par[2]
   # Computation
   value = ( A + B * x ) * math.exp( - x/tau )
   return value

#
# Main program
#

xmin = 0
xmax = 10

# Define a ROOT function object using user-defined funtion implementation
func_user = TF1("func_user", myfunc1D, xmin, xmax, myfunc1D_npar)
func_user.SetParameters(5,100,1)

# Define a ROOT function using ROOT functions library
func_lib = TF1("func_lib", "[0]*TMath::Landau(x,[1],[2])", xmin, xmax)
func_lib.SetParameters(100, 2, 1)

# Define a ROOT function using a simple expression
func_formula = TF1("func_formula", "([0] + [1]*x + [2] * x*x)*(1+sin([3]*x))", xmin, xmax)
func_formula.SetParameters(0.05, 0.1, 0.2, 6)
# Default function graphs have 400 points, this can be increased
# for a more smooth look
func_formula.SetNpx(1000)

# Draw all on a single figure
ymin = np.amin([ func_user.GetMinimum(), func_lib.GetMinimum(), func_formula.GetMinimum() ])
ymax = np.amax([ func_user.GetMaximum(), func_lib.GetMaximum(), func_formula.GetMaximum() ])

# Set up dummy histogram
nbins = 100
plotspace = TH2F("plotspace", "Examples of functions", nbins, xmin, xmax,
                 nbins, ymin*1.2, ymax*1.2)
plotspace.GetXaxis().SetTitle("x value")
plotspace.GetYaxis().SetTitle("y value")

# Set up canvas
canvas = TCanvas("canvas","My figure", 10,10,800, 500)
canvas.Draw()
canvas.cd() # not strictly necessary

ROOT.gStyle.SetOptStat(0)   # Switch off plot statistics window

# Graph drawing options
func_user   .SetLineColor(ROOT.kRed)
func_lib    .SetLineColor(ROOT.kBlue)
func_formula.SetLineColor(ROOT.kMagenta)

func_user   .SetLineWidth(3)
func_lib    .SetLineWidth(3)
func_formula.SetLineWidth(3)

# Draw everything
plotspace.Draw()
func_user.Draw("same")
func_lib.Draw("same")
func_formula.Draw("same")
