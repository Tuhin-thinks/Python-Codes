#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    vector<string> user_name;

    user_name = {"Tuhin", "John", "Doe", "Roger", "Fred", "Alen"};

    sort(user_name.begin(), user_name.end());

    cout << "Names in ascending order:\n";
    for(auto x:user_name){
        cout << x << endl;
    }

    
    return 0;
}