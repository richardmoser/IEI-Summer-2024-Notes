from ROOT import TFile, TTree, TH1F, TGraph
from ROOT import TCanvas

# Open ROOT file for reading
file_in = TFile("simdata.root")

# Retrieve from the file the tree with event data
tree = file_in.Get("tree")

# Prepare a histogram for SNR
hist = TH1F("hist_SNR", "Signal events SNR", 100, 0, 20)
hist.GetXaxis().SetTitle("SNR")

# Prepare a graph for one waveform
special_event_number = 17
waveform_graph = TGraph()
waveform_graph.GetXaxis().SetTitle("time [ns]")
waveform_graph.GetYaxis().SetTitle("voltage [millivolts]")
waveform_graph.GetYaxis().SetTitleOffset(1.4)
waveform_graph.SetTitle("Waveform for the event {}".format(special_event_number))

# Loop over events
n_events = tree.GetEntries()
for i_event in range(n_events):

    # Load this event into memory
    # After this call, one can access variables for this event as tree.varname
    tree.GetEntry(i_event)

    # Add the SNR value in this event to the SNR histogram
    hist.Fill( tree.SNR )

    # For the event of interest, save the waveform into a graph
    if tree.event_number == special_event_number :
        for i_point in range( tree.n_points ):
            time = tree.waveform_time[i_point]
            volt = tree.waveform_volt[i_point]
            waveform_graph.SetPoint( waveform_graph.GetN(), time, volt )

# Prepare canvas and draw
canvas = TCanvas("canvas","My figure", 10,10, 1000, 500)
canvas.Draw()
canvas.Divide(2,1)

canvas.cd(1)
hist.Draw()

canvas.cd(2)
waveform_graph.Draw()
