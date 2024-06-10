/*
    Author: Richard Moser
    Date: 05Jun24
    Description: This program reads in data from an array and fits the data to a polynomial of degree 1-5. The data is
    then plotted on a graph with the fits.
    Data Source: https://www.kaggle.com/datasets/starbucks/starbucks-menu
    Requirements: ROOT (https://root.cern.ch/)
    Instructions to run:
        1: Open your terminal
        2: Navigate to the directory containing this file
        3: source /path/to/root/bin/thisroot.sh if you have not already done so in the .bashrc file
        4: either type root and then .x fitting.C or type root -l fitting.C
*/



void fitting()
{
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

    // set x is the range of values in the energy_array and y is the number of events per energy value bin
    int bins = 100;
    TH1F *hist = new TH1F("hist", "Histogram", bins, 0, 1000000);
    //    creates new TH1F named hist

    for (int i = 0; i < 10000; i++)
    {
        hist->Fill(energy_array[i]);
    }

    hist->GetXaxis()->SetNoExponent();
//    keeps the x-axis from being in scientific notation (it wants to scale by a factor of 10^3)


    hist->GetXaxis()->SetNdivisions(5);
//    Only shows 5 divisions on the x-axis



    TCanvas *c1 = new TCanvas();
    //    creates new TCanvas named c1
    c1->SetWindowSize(1000, 800);
    //    sets the window size of the TCanvas

    c1->SetLogx();
    c1->SetLogy();
//    sets the x and y-axis to be logarithmic

    hist->SetTitle("Fitting Tutorial Plot");
    // sets the title fo the hist to "Starbucks Drink Nutrition"

    hist->GetXaxis()->SetTitle("Number of Events");
    hist->GetYaxis()->SetTitle("Energy (Gev)");
    hist->SetMarkerStyle(4);
    hist->SetMarkerSize(2);


    // set a custom fit for a log-log plot of the form y intercept + slope * log(x)
    // log should be in log base 10
//    TF1 *custom_fit = new TF1("custom_fit", "10 ** ([0] + [1]*log(x))", 0, 1000000);
    TF1 *custom_fit = new TF1("custom_fit", "[0]*TMath::Power(x,[1])", 0, 1000000);
//    TF1 * f1 = new TF1("f1","[0]*TMath::Power(x,[1])");

    custom_fit->SetParameter(0, 1);
    custom_fit->SetParameter(1, 1);
    hist->Fit("custom_fit", "+");
    // fits the hist with a custom fit

    hist->GetFunction("custom_fit")->SetLineColor(kMagenta);

    // add a legend
    TLegend *legend = new TLegend(0.65, 0.65, 0.89, 0.89);
    // (x1, y1, x2, y2) where x1 and y1 are the coordinates of the bottom left corner of the legend and x2 and y2 are the
    // coordinates of the top right corner of the legend

    legend->AddEntry(hist->GetFunction("custom_fit"), "custom_fit", "l");

    hist->SetStats(0);
    // removes the stats box from the histogram

    legend->Draw();
    c1->Update();
    c1->Draw();

    char bob = 0;
//    while (bob == 0)
//        cin >> bob;
    // this is a janky workaround to keep the canvas open until the user presses enter. If you don't close the canvas
    // by way of code, it will stay open until you manually close the window. If you don't set some kind of wait
    // condition, the canvas will close immediately after it is drawn. Basically we are exploiting the fact that C/C++
    // will wait for an input when you call cin. Here we are writing whatever you type to the char bob and then doing
    // nothing with it.
//    c1->Close();
}

