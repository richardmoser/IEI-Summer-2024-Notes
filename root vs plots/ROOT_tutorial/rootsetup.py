#
# Load ROOT libraries in Jupyter notebook
# The line below assumes that the Jupyter kernel is py3-4.3.0: icetray/v1.9.2
#
import sys
sys.path.append('/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/Ubuntu_20.04_x86_64/lib/root')
import ROOT
#
# This line below enables graphical output from ROOT
#
%jsroot on
