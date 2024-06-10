from ROOT import TGraph
from ROOT import TCanvas

# Create empty graph
graph = TGraph() 

# Add points to the graph
# Note: the graph object has points from 0 to N-1. The call
# GetN() returns the total number of points N, so SetPoint here
# just adds one more point at the end.
graph.SetPoint( graph.GetN(), 3, 5)
graph.SetPoint( graph.GetN(), 4, 5)
graph.SetPoint( graph.GetN(), 5, 7)
graph.SetPoint( graph.GetN(), 6, 6)
graph.SetPoint( graph.GetN(), 7, 10)
graph.SetPoint( graph.GetN(), 8, 11)

# Prepare graphical window: open a canvas                                                                                             
c1 = TCanvas("c1","c1",800,800)
c1.Draw()

# Draw the graph with all default options
# on a default canvas
graph.Draw()

