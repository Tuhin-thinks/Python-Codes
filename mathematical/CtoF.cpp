/**
 * problem statement: https://practice.geeksforgeeks.org/problems/convert-celsius-to-fahrenheit/1/?track=DSASP-Mathematics&batchId=154#
 * */
#include <math.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

class Solution{
    public:

    double CtoF(double C){
        double F = (C / 5.0 * 9.0) + 32;
        return F;
    }
};

int main(){
    int T;
    int C, F;
    cin >> T;  // input number of test cases
    while (T){
        cin >> C; // input celcius in integer
        Solution ob;
        cout << floor(ob.CtoF(C)) << endl;
        T--;
    }
    return 0;
}