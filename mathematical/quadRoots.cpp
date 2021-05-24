#include <iostream>
#include <stdlib.h>
#include <vector>
#include <math.h>

using namespace std;

class Solution{
    public:

    vector<int> quadraticRoots(int a, int b, int c){
        vector<int> roots;

        int roots_sum, roots_diff;
        double d = b*b - (4*a*c);
        if (d < 0){
            roots.push_back(-1);
            return roots;
        }
        roots_sum = floor((-b + sqrt(d))/(2*a));
        roots_diff = floor((-b - sqrt(d))/(2*a));

        cout << "d=" << d << endl;
        
        roots.push_back(roots_sum);
        roots.push_back(roots_diff);

        return roots;
    }
};

int main(){

    int T,a, b, c;
    cin >> T;
    while(T){
        cin >> a >> b >> c;
        Solution ob;
        vector<int> roots = ob.quadraticRoots(a, b, c);
        if(roots.size() == 1 && roots[0]==-1){
            cout << "Imaginary";
        }
        else
            for(int i=0; i<roots.size();i++) cout << roots[i] << "  ";
        T--;
        cout << endl;
    }

    return 0;
}