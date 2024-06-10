import numpy as np
import math
import ROOT
from ROOT import TH2F # TH2F - float, TH2D - double precision
from ROOT import TRandom
from ROOT import TStyle
from ROOT import TCanvas
from ROOT import TPad

# Histogram binnings
xlo = 0
xhi = 70
nbins_x = 20
ylo = 0
yhi = 70
nbins_y = 30

binning_x = np.linspace(xlo, xhi, nbins_x + 1)
binning_y = np.linspace(ylo, yhi, nbins_y + 1)

hist = TH2F("hist", "Data on (#xi_{1}, #xi_{2}) events", nbins_x, binning_x, nbins_y, binning_y)
# Alternatively: hist = TH2F("hist", "My histogram", nbins_x, xlo, xhi, nbins_y, ylo, yhi)

# Set histogram attributes
hist.GetXaxis().SetTitle("Observable #xi_{1}")   # used Latex math symbol here
hist.GetYaxis().SetTitle("Observable #xi_{2}")   
hist.GetZaxis().SetTitle("Number of events")   
hist.GetXaxis().SetTitleOffset(1.2)
hist.GetYaxis().SetTitleOffset(1.2)
hist.GetZaxis().SetTitleOffset(1.5)

# We will fill the histogram with random sets of (x,y) pairs.
# The x and y are distributed according to Gaussians, and are correlated
mean1  = 20
sigma1 = 5
mean2  = 25
sigma2 = 7
rho = 0.7    # correlation coefficient

generator = TRandom()
n_events = 10000

# Create all events and put them into a 2D histogram
for iEvent in range(n_events):
    x_value = generator.Gaus(mean1, sigma1)
    y_tmp   = generator.Gaus(mean2, sigma2)
    y_value = rho * x_value + math.sqrt( 1 - rho**2 ) * y_tmp
    hist.Fill(x_value, y_value)

# Tweak style of the plots as needed
style = TStyle("Plain","Plain Style")
style.SetOptStat(0) # Disable histogram status box drawing (optional)
style.SetPalette(1) # Color palette for the 3d dimension, one of several possible ones
style.cd() # Make this style the current style

# Set up canvas for the figures
canvas1 = TCanvas("canvas1", "2D histogram example", 10,10,1000,1000)
canvas1.Draw()
canvas1.Divide(2,2)

# Draw first subplot
canvas1.cd(1)
ROOT.gPad.SetRightMargin(0.20)
hist.Draw("colz") # use "heatmap" color plot for Z axis

# Draw second subplot
canvas1.cd(2)
hist.Draw("box")

# Draw third subplot
canvas1.cd(3)
hist.Draw("cont")

# Draw forth subplot
canvas1.cd(4)
hist_copy = hist.Clone("hist copy")  # Make a copy to draw with different settings
hist_copy.GetXaxis().SetTitleOffset(2)
hist_copy.GetYaxis().SetTitleOffset(2)
hist_copy.GetZaxis().SetTitleOffset(1.6)
hist_copy.Draw("surf")


