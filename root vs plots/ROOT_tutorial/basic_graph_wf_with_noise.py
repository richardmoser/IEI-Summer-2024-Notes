import numpy as np
import math
import ROOT
from ROOT import TGraph
from ROOT import TCanvas
from ROOT import TH2F
from ROOT import TLegend
from ROOT import TRandom

# Define useful functions

# Define a burst radio signal
def burst_waveform( time ):
    A = 250.0
    B = 10.0
    C = 10.0
    omega = 1.2
    k = 1.0

    cosine_term   = A * math.cos( omega * time )      # oscillation
    heaviside_term = 1 / (1 + math.exp( -2*k*time ) ) # turn-on (heaviside step function parameterized)
    exponent_term = math.exp( -(time - B)/C )         # attenuation 

    voltage = cosine_term * heaviside_term * exponent_term
    return voltage

#
# Main program starts here
#

# Set up time base for our graphs
tmin = -250
tmax = +250
n_points = 1000
time_array = np.linspace(tmin, tmax, n_points)

# Generator for random noise
generator = TRandom()
noise_mean = 0
noise_amplitude = 50 # in millivolts

# Create empty graph
graph = TGraph() 
# Add points one by one
for time in time_array:
    voltage = burst_waveform( time ) + generator.Gaus(noise_mean, noise_amplitude)
    graph.SetPoint( graph.GetN(), time, voltage )

# === The drawing section ==-

# Create a "dummy" histogram that is the template for drawing for 
# convenient access to X, Y axes and various plot settings

# Find the min and max values of the voltage
voltage_max = np.amax( graph.GetY() )
voltage_min = np.amin( graph.GetY() )

nbins_dummy = 100
plotspace = TH2F("plotspace", "Waveform with signal and noise", nbins_dummy, tmin, tmax, 
                 nbins_dummy, voltage_min * 1.2, voltage_max * 1.2)

plotspace.GetXaxis().SetTitle("time [ns]")
plotspace.GetYaxis().SetTitle("voltage [millivolts]")
plotspace.GetYaxis().SetTitleOffset(1.0)

# Create canvas
canvas = TCanvas("canvas","My figure", 10,10,800, 500)
canvas.Draw()
canvas.cd() # not strictly necessary

ROOT.gStyle.SetOptStat(0)   # Switch off plot statistics window

# Set up graphs options
graph.SetLineColor(ROOT.kBlue)
graph.SetLineWidth(3)

# Draw the dummy histogram and the graphs
plotspace.Draw()
graph.Draw("same,L") # draw as a line without markers

