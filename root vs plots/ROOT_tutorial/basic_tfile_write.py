from array import array
from ROOT import TFile, TTree, TGraph, TH1F, TF1

# Create some simple ROOT objects
hist = TH1F("hist","My hist", 100, 0, 1)
hist.Fill(0.2)
hist.Fill(0.3)

graph = TGraph()
graph.SetPoint( graph.GetN(), 1, 2.5)
graph.SetPoint( graph.GetN(), 2, 17.0)

func = TF1("func","[0] + x*[1]", 0, 10)
func.SetParameters(1,2)

# Open new file for writing
file_out = TFile('test.root','recreate')
file_out.cd() # really needed only if there are multiple open files

# Create an example tree. Note that unlike simple objects above it is generally
# a good idea (but not required) to create tree after opening the file for writing.
# In case if the tree becomes very large, like 2GB, it will be then kept on disk
# and not in memory.
tree = TTree('tree','Test tree')
# Variables for the tree
var1 = array('i',[0])
var2 = array('f',[0.])
# Tree structure
tree.Branch('var1',var1,'var1/I') 
tree.Branch('var2',var2,'var2/F') 
# Tree data, just enter one event in this example
var1 = 1
var2 = 2.5
tree.Fill()

# Save into file, the one currently open into which we cd()'ed above
hist.Write()
graph.Write("mygraph")  # the optional argument sets the name of the graph
func.Write()
tree.Write()

file_out.Close()



