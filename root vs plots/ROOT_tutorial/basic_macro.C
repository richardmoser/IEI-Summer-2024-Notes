{

  // Declare some varialbles and fill them
  float x=5;
  float y = x+6;
  std::vector<float> myvector;
  myvector.push_back(x);
  myvector.push_back(y);

  // Run a basic loop, print
  for(uint i=0; i<myvector.size(); i++){ 
    std::cout << myvector[i] << std::endl;
  } // end loop over the vector

}
