import numpy as np
import ROOT
from ROOT import TH1F
from ROOT import TRandom
from ROOT import TCanvas
from ROOT import TLegend

xlo = 0
xhi = 50
nbins = 50

binning = np.linspace(xlo, xhi, nbins+1)

hist1 = TH1F("hist1", "My histogram", nbins, binning)
hist2 = TH1F("hist2", "My histogram", nbins, binning)
# Alternatively: hist = TH1F("hist", "My histogram", nbins, xlo, xhi)

# Fill histogram with Poisson-distributed random numbers
generator = TRandom()  # generic generator object
val_expected = 12      # example mean value for Poisson distribution
nEvents = 10000     # total number of observation
for iEvent in range(nEvents):
    val = generator.Poisson(val_expected)
    hist1.Fill(val)

# Fill another histogram with a distribution with different expectation
val_expected = 20
for iEvent in range(nEvents):
    val = generator.Poisson(val_expected)
    hist2.Fill(val)
    
# Prepare for drawing: configure histogram attributes.
# These all can be left default

# Histogram lines
hist1.SetLineColor(ROOT.kRed)
hist1.SetLineWidth(2)
hist2.SetLineColor(ROOT.kBlue)
hist2.SetLineWidth(2)

# Histogram markers
hist1.SetMarkerStyle(20)
hist1.SetMarkerSize(1.5)
hist1.SetMarkerColor(ROOT.kRed)
hist2.SetMarkerStyle(21)
hist2.SetMarkerSize(1.5)
hist2.SetMarkerColor(ROOT.kBlue)

# Histogram fills
hist1.SetFillColor(46) # See color codes in TAttFill docs
hist1.SetFillStyle(3244) # See patternstyles in TAttFill docs
hist2.SetFillColor(38) 
hist2.SetFillStyle(3011) 


# Switch off statistics window on all figures
ROOT.gStyle.SetOptStat(0) # gStyle is a global variable of the TStyle class

# For histogram titles, it is sufficient to set them on the first histogram drawn
hist1.GetXaxis().SetTitle("observed count")
hist1.GetYaxis().SetTitle("number of occurrances")

# Make a canvas for plotting a single figure
canvas1 = TCanvas("cv1", "My canvas 1", 10,10,600, 600)
canvas1.Draw()
canvas1.cd()

# This call is optional: use it when the axis title does not fit. 
# gPad is the current drawing pad, object of TPad class
# Default margins are 0.1, i.e. (10%). Also one can do Right, Top, Bottom
ROOT.gPad.SetLeftMargin(0.15)

# Draw the histograms
hist1.Draw("hist")
hist2.Draw("hist, same")

#Make another canvas for plotting several figures
canvas2 = TCanvas("cv2", "My canvas 2", 50,10,1000, 500)
canvas2.Draw()
canvas2.Divide(2,1)
canvas2.cd(1)
ROOT.gPad.SetLeftMargin(0.15) # optional, if axis title doesn't fit

# Draw histogram with markers and errors on the first subfigure
hist1.Draw("PLE")
hist2.Draw("PE, same")

# Proceed to the second subfigure
canvas2.cd(2)
ROOT.gPad.SetLeftMargin(0.15) # optional, if axis title doesn't fit

# Draw hists
hist1.Draw("PE,hist")
hist2.Draw("hist,same")

# Draw legend
legend = TLegend(0.6, 0.7, 0.85, 0.85)
legend.AddEntry(hist1, "Expected 12", "P") # Can use F - fill, L - line, P - markers
legend.AddEntry(hist2, "Expected 20", "FL")
legend.Draw("same")


