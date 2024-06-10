 
void histtut()
{

        TCanvas *c1 = new TCanvas();
//     creates new TCanvas named c1
    c1->SetWindowSize(800, 1200);
//    sets the window size of the TCanvas

    c1->Divide(1, 2);
//    divides the canvas into 2 pads, 1 row, 2 columns


    c1->cd(1);
//    sets the current pad to the first pad (like changing directories in the terminal)

    int bins = 100;
    TH1F *hist = new TH1F("hist", "Histogram", bins, 0, 1000000);
//    creates new TH1F named hist
//    TH1 *name_of_histogram = new TH1F(name, title, bins, start value, end value)

    double energy_array[9999];
//    C/C++ arrays are a pain so you have to specify the size of the array at the moment you create it so that the
//    compiler knows how much memory to allocate. In this case I know that the file energy_data_1.txt has 1000 entries.

//    open the file energy_data_1.txt and read the data into an array
    ifstream file("energy_data_1.txt");
    if (file.is_open())
    {
        for (int i = 0; i < 10000; i++)
        {
            file >> energy_array[i];
        }
        file.close();
    }
    else
    {
        cout << "Unable to open file" << endl;
    }
//    print the first 5 entries of energy_array
    for (int i = 0; i < 5; i++)
    {
        cout << energy_array[i] << endl;

    }

//    fill the histogram with the data from the array
    for (int i = 0; i < 10000; i++)
    {
        hist->Fill(energy_array[i]);
    }


    hist->GetXaxis()->SetNoExponent();
//    keeps the x-axis from being in scientific notation (it wants to scale by a factor of 10^3)

    hist->GetXaxis()->SetTitle("Energy (GeV)");
    hist->GetYaxis()->SetTitle("Number of Events");
    hist->SetTitle("This plot is in linear x and y scale");
//    Sets the title of the axes and histogram

    hist->GetXaxis()->SetNdivisions(5);
//    Only shows 5 divisions on the x-axis



    hist->Draw();
//    draws the histogram on the canvas

    c1->cd(2);
//    sets the current pad to the second pad

// recreate the histogram with a logarithmic y-axis
    TH1F *hist_log = new TH1F("hist_log", "Histogram", bins, 0, 1000000);
//    creates new TH1F named hist_log

    for (int i = 0; i < 10000; i++)
    {
        hist_log->Fill(energy_array[i]);
    }

    hist_log->GetXaxis()->SetNoExponent();
//    keeps the x-axis from being in scientific notation (it wants to scale by a factor of 10^3)

    hist_log->GetXaxis()->SetTitle("Energy (GeV)");
    hist_log->GetYaxis()->SetTitle("Number of Events");
    hist_log->SetTitle("This plot is in log x and y scale");
//    Sets the title of the axes and histogram

    hist_log->GetXaxis()->SetNdivisions(5);
//    Only shows 5 divisions on the x-axis

    gPad->SetLogy();
    gPad->SetLogx();
//    sets the x and y-axis to be logarithmic

    hist_log->Draw();
//    draws the histogram on the canvas


}

