#include <map>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool is_anagram(string subject, string anagram){
    map<char, int> subject_map;
    map<char, int> anagram_map;

    for(int i = 0; i< subject.size(); i++){
        map<char, int>::iterator it = subject_map.find(subject[i]);
        if (it == subject_map.end()){
            subject_map.insert({subject[i], 1});
        }
        else{
            it->second += 1;
        }
    }
    for(int i = 0; i< anagram.size(); i++){
        map<char, int>::iterator it = anagram_map.find(anagram[i]);
        if (it == anagram_map.end()){
            anagram_map.insert(pair<char, int>(anagram[i], 1));
        }
        else{
            it->second += 1;
        }
    }

    return subject_map.size() == anagram_map.size() && equal(
        subject_map.begin(), subject_map.end(), anagram_map.begin(), [] (auto a, auto b){
        return a.first == b.first && a.second == b.second;
    });
}

int main(){
    fstream newfile;
    vector<string> words;
    int limit = 10000, i = 0;

    newfile.open("words_alpha.txt", ios::in);
    if (newfile.is_open()){
        string tp;
        while (getline(newfile, tp)){
            cout << tp << endl;
            words.push_back(tp);
            if (i == limit){
                break;
            }
            i++;
        }
        newfile.close();
    }
    cout << "Total number of words : " << words.size() << endl;

    int length2;
    cout <<  "Enter size of anagrams you want to list :";
    cin >> length2;

    int N = words.size();

    for(i=0; i<N; i++){
        if (words.at(i).size()==length2){
            for (int j=i+1; j<N; j++){
                if (is_anagram(words.at(i), words.at(j))){
                    cout << words.at(i) + ", " + words.at(j) << "\n";
                    }
            }
        }
    }


}