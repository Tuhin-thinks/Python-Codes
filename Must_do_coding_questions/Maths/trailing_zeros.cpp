#include<bits/stdc++.h> 
using namespace std; 

 // } Driver Code Ends


//User function Template for C++
class Solution
{
public:
    int factorial(int n){
    int f = 1;
    while(n > 1){
        cout << f << endl;
        f = f*n;
        n -= 1;
    }
    return f;
    }
    int trailingZeroes(int N)
    {
        int f = factorial(N);
        cout << "factorial = " << f << endl;
        int trail = 0;
        while(f){
            if(f%10 == 0){
                trail += 1;
                f = int(f / 10);
            }
            else{
                return trail;
                break;
            }
        }
        
        return 0;
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin >> N;
        Solution ob;
        int ans  = ob.trailingZeroes(N);
        cout<<ans<<endl;
    }
    return 0;
}  // } Drive