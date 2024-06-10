from array import array
import ROOT

# Create the tree
tree = ROOT.TTree("tree", "An Example Tree")

# Declare variables that we will save for each event in a certain way
event_number   = array('i', [0])
SNR            = array('f', [0.])

# Tell the tree what will be stored in it
# First argument: variable name as will be seen in the tree
# Second argument: what value of variable to use to put into the tree
# Third argument: gives the type (integer, floating point, array, char, ...)
tree.Branch("event_number"  , event_number, 'event_number/I')
tree.Branch("SNR"           , SNR,          'SNR/F')

# Put into the tree data event by event
# Note: simple int/float variables are actually arrays which have one element,
# hence [0] below for each event.

# First event
event_number[0] = 0
SNR[0] = 2.34
tree.Fill()   # this stores the event in the tree

# Second event
event_number[0] = 1
SNR[0] = 7.954
tree.Fill()   # this stores the event in the tree

# Print tree structure as a check
tree.Print()

