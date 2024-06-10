import numpy as np
from array import array
import ROOT
from ROOT import TRandom

# Declare the tree
tree = ROOT.TTree("tree", "Simple neutrino data")

# Need to decide beforehand on the length of the waveforms
n_waveform_points = 1000

# Declare variables that we will save for each event in a certain way
event_number   = array('i', [0])   # integer number
event_type     = array('i', [0])   # integer number
SNR            = array('f', [0.])  # floating point number
n_points       = array('i', [n_waveform_points])   # integer number
waveform_time = array('f', n_waveform_points*[0.]) # integer number
waveform_volt = array('f', n_waveform_points*[0.]) # integer number

# Tell the tree what will be stored in it
tree.Branch("event_number"  , event_number, 'event_number/I')
tree.Branch("event_type"    , event_type,   'event_type/I')
tree.Branch("SNR"           , SNR,          'SNR/F')
tree.Branch("n_points"      , n_points,     'n_points/I') # The array length is stored explicitly
tree.Branch("waveform_time" , waveform_time, 'waveform_time[n_points]/F')
tree.Branch("waveform_volt" , waveform_volt, 'waveform_volt[n_points]/F')

# Generate events one by one in a loop.
generator = TRandom()
signal_event_fraction = 0.2
n_events = 1000
for i_event in range(n_events):

    # Event number is just the event index
    event_number[0] = i_event

    # Generate event type
    random_number = generator.Rndm()
    if random_number < signal_event_fraction :
        # event_type_string = "signal" 
        event_type[0] = 0
    else:
        # event_type_string = "noise" 
        event_type[0] = 1

    # Generate waveform
    t0 = 0
    dt = 0.5
    noise_amplitude = 30
    for i_point in range(n_waveform_points):
        waveform_time[i_point] = t0 + dt * i_point
        waveform_volt[i_point] = generator.Gaus(0.0, noise_amplitude)
        # Add a spike in the middle for signal events
        if event_type[0] == 0:
            if i_point == int(n_waveform_points/2) :
                waveform_volt[i_point] += noise_amplitude*10

    # Compute Signal-to-Nose as the peak voltage divided by the noise level
    Vrms  = np.std( np.array( waveform_volt ) )
    Vpeak = np.amax( abs(np.array( waveform_volt ) ) )
    SNR[0] = Vpeak/Vrms

    # Save data in the tree
    tree.Fill()

# Print tree structure as a check
tree.Print()

