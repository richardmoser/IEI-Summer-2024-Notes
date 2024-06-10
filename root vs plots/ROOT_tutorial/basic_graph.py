import numpy as np
import math
import ROOT
from ROOT import TGraph
from ROOT import TCanvas
from ROOT import TH2F
from ROOT import TLegend

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

# Define sine wave radio signal
def sin_waveform( time ):
    A = 100      # amplitude
    omega = 1.0  # angular frequency
    voltage = A * math.sin( omega * time )
    return voltage

#
# Main program starts here
#

# Set up time base for our graphs
tmin = -50
tmax = +50
n_points = 1000
time_array = np.linspace(tmin, tmax, n_points)

# === Create graph with the first method ===

# Create empty graph
graph_burst = TGraph() 
# Add points one by one
for time in time_array:
    voltage = burst_waveform( time )
    graph_burst.SetPoint( graph_burst.GetN(), time, voltage )

# === Create graph with the second method ===

# Create the voltage array (the time array is already created above)
voltage_array = np.array([ ])
for time in time_array:
    voltage = sin_waveform( time )
    voltage_array = np.append(voltage_array, voltage)

# Create the graph given X- and Y- arrays (i.e. time and voltage arrays)
graph_sin = TGraph(n_points, time_array, voltage_array)

# === The drawing section ==-

# Create a "dummy" histogram that is the template for drawing for 
# convenient access to X, Y axes and various plot settings

# Find the min and max values of the voltage between the two graphs
all_voltages_array = np.append( np.array( graph_burst.GetY() ), np.array( graph_sin.GetY() ) )
voltage_max = np.amax( all_voltages_array)
voltage_min = np.amin( all_voltages_array)

nbins_dummy = 100
plotspace = TH2F("plotspace", "", nbins_dummy, tmin, tmax, 
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
graph_burst.SetLineColor(ROOT.kRed)
graph_burst.SetLineWidth(3)
graph_sin.SetLineColor(ROOT.kBlue)
graph_sin.SetLineWidth(3)

# Draw the dummy histogram and the graphs
plotspace.Draw()
graph_burst.Draw("same,L") # draw as a line without markers
graph_sin.Draw("same,L")

# Add a legend to the plot
legend = TLegend(0.15, 0.15, 0.4, 0.3)
legend.AddEntry(graph_burst, "Burst model", "L")
legend.AddEntry(graph_sin, "Sin wave model", "L")
legend.Draw("same")

canvas.Print("myplot.pdf")
