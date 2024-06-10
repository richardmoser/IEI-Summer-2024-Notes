
In this area, a number of examples for ROOT usage are found.

For ROOT with python, both python and ROOT needs to be installed.
On Cobalt at the IceCube computing facility at the University of Wisconsin-Madison
one can set up already installed ROOT/python as follows:

   source /cvmfs/ara.opensciencegrid.org/trunk/centos7/setup.sh

If not on Cobalt, one needs to make sure that python is installed (3.x), make
sure ROOT is installed, and don't forget to tun $ROOTSYS/thisroot.sh,
which among other things adds pyroot package location to the path of python.
