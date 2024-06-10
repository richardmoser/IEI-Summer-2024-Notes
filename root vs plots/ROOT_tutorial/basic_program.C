#include <iostream>
#include <vector>

void basic_program(){ // If run from ROOT with .x, match main function
                      // name to the file name

  // Declare some varialbles and fill them
  float x = 5;
  float y = x+6;
  vector <float> myvect;
  myvect.push_back(x);
  myvect.push_back(y);

  // Execute a loop and print
  for(uint i=0; i<myvect.size(); i++) {
    cout << myvect[i] << endl;
  } // end for loop over the vector

  return;
}


