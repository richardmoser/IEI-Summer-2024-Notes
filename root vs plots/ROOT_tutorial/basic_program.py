# Import needed packages
import ROOT
import numpy as np

# Define variables
x = 5
y = x+6
myvector = np.array([ ])
myvector = np.append( myvector, x)
myvector = np.append( myvector, y)

# Execute a loop and print
for element in myvector:
        print(element)
