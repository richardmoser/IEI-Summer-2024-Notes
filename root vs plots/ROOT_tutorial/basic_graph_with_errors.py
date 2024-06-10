import numpy as np
import ROOT
from ROOT import TGraphErrors
from ROOT import TH2F
from ROOT import TCanvas
from ROOT import TRandom

# Simple quadratic dependence
def quadratic_function(var):
    A = 10
    B = 3
    C = 2
    return A + B * var + C * var**2

# Suppose error scales linearly with the value
def relative_error(var):
    A = 0.02
    return A*var

#
# Main program
#

# Define X axis.
# We will need the X values and X errors, the latter are half-distance between data points along X
# However, X and X errors do not have to be as in regular binning/equally space, can be arbitrary
xmin = 0.0
xmax = 10.0
n_points = 20
binning = np.linspace(xmin, xmax, n_points+1)
x_array = (binning[:-1] + binning[1:] )/2
x_err_array = np.ediff1d( binning ) / 2

# Make up data points with randomization according to errors
# Start with preparing the generator
generator = TRandom()

# Create numpy arrays for Y and error on Y
y_array = np.array([ ])
y_err_array = np.array([ ])

# Fill the arrays
for x in x_array:
    y_expected  = quadratic_function( x )
    y_err       = y_expected * relative_error( x )
    y           = generator.Gaus( y_expected, y_err )
    y_array     = np.append( y_array, y )
    y_err_array = np.append( y_err_array, y_err )

# Create the graph object
graph = TGraphErrors(n_points, x_array, y_array, x_err_array, y_err_array)
# Set up graphs options
graph.SetLineColor(ROOT.kBlue)
graph.SetLineWidth(3)
graph.SetMarkerStyle(25)
graph.SetMarkerColor(ROOT.kBlue)
graph.SetMarkerSize(1.0)

# Create dummy histograph for defining the space
ymax = np.amax( y_array ) + np.amax( y_err_array )
ymin = np.amin( y_array ) - np.amax( y_err_array )

nbins_dummy = 100
plotspace = TH2F("plotspace", "Example graph with errors", nbins_dummy, xmin, xmax, 
                 nbins_dummy, ymin * 1.2, ymax * 1.2)

plotspace.GetXaxis().SetTitle("x value")
plotspace.GetYaxis().SetTitle("y value")
plotspace.GetYaxis().SetTitleOffset(1.0)

# Create canvas
canvas = TCanvas("canvas","My figure", 10,10,800, 500)
canvas.Draw()
canvas.cd() # not strictly necessary

ROOT.gStyle.SetOptStat(0)   # Switch off plot statistics window

# Draw everything
plotspace.Draw()
graph.Draw("same, PE")   # Draw with markers and error bars
