import numpy as np
from ROOT import TH2F # TH2F - float, TH2D - double precision
from ROOT import TCanvas

# Histogram binnings
xlo = 0
xhi = 50
nbins_x = 20
ylo = 0
yhi = 50
nbins_y = 30

binning_x = np.linspace(xlo, xhi, nbins_x + 1)
binning_y = np.linspace(ylo, yhi, nbins_y + 1)

hist = TH2F("hist2", "My histogram", nbins_x, binning_x, nbins_y, binning_y)
# Alternatively: hist = TH2F("hist", "My histogram", nbins_x, xlo, xhi, nbins_y, ylo, yhi)

# Fill histogram with numbers
hist.Fill(5, 6)
hist.Fill(5, 7)
hist.Fill(9, 3)
hist.Fill(9, 3)

# Prepare graphical window: open a canvas                                                                                             
c1 = TCanvas("c1","c1",800,800)
c1.Draw()

# Draw histogram in most basic way
hist.Draw("box")

