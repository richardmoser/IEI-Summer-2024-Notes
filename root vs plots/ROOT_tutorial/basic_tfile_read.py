from ROOT import TFile, TTree, TGraph, TH1F, TF1

# Open ROOT file for reading
file_in = TFile("test.root")

# List file content
file_in.ls()

# Get all the objects
tree = file_in.Get("tree")
hist = file_in.Get("hist")
graph = file_in.Get("graph")
func = file_in.Get("func")

# Now one can do any manipulations with the objects (drawing, fitting, etc)

