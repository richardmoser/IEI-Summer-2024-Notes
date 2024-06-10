#
# This is a brief bit of code to make a few plots in Jupyter notebooks
# It assumes that the following scripts are already loaded and executed in the same session:
#   basic_ttree.py
#   basic_ttree_examine.py
from ROOT import TCanvas

# Look at the tree a print a few things:
examine(tree)

# Draw 1D signal-to-noise figure for all events
c1 = TCanvas("c1","c1",500,500)
c1.Draw()
#
draw_SNR(tree)

# Draw 1D signal-to-noise figure for all events
c2 = TCanvas("c2","c2",500,500)
c2.Draw()
#
draw_signal_SNR(tree)

# Draw 2D figure of signal-to-noise vs event type for all events
c3 = TCanvas("c3","c3",500,500)
c3.Draw()
#
draw_SNR_vs_type(tree)



