/*
Problem Statement:
Anagram of String 
Given two strings S1 and S2 in lowercase, the task is to make them anagram. The only allowed operation is to remove a character from any string. Find the minimum number of characters to be deleted to make both the strings anagram. Two strings are called anagram of each other if one of them can be converted into another by rearranging its letters.

Example 1:

Input:
S1 = bcadeh
S2 = hea
Output: 3
Explanation: We need to remove b, c
and d from S1.
Example 2:

Input:
S1 = cddgk
S2 = gcd
Output: 2
Explanation: We need to remove d and
k from S1.
Your Task:
Complete the function remAnagram() which takes two strings S1, S2 as input parameter, and returns minimum characters needs to be deleted.

Expected Time Complexity: O(max(|S1|, |S2|)), where |S| = length of string S.
Expected Auxiliary Space: O(26)

Constraints:
1 <= |S1|, |S2| <= 10^5
*/

#include <stdlib.h>
#include <iostream>
#include <string>
using namespace std;

const int CHARS = 26;

int remAnagram(string str1, string str2);

int main(){
    int t;
    cin>>t;

    while (t--)
    {
        string str1, str2;
        cin>>str1>>str2;
        cout<<remAnagram(str1, str2);
        cout<<endl;
    }
    return 0;
    

}

int remAnagram(string str1, string str2)
{
// Your code goes here
    int count1[CHARS] = {0}, count2[CHARS] = {0}; 
  
    // count frequency of each character in first string 
    for (int i=0; str1[i]!='\0'; i++) 
        count1[str1[i]-'a']++; 
  
    // count frequency of each character in second string 
    for (int i=0; str2[i]!='\0'; i++) 
        count2[str2[i]-'a']++; 
  
    // traverse count arrays to find number of characters 
    // to be removed 
    int result = 0; 
    for (int i=0; i<26; i++) 
        result += abs(count1[i] - count2[i]); 
    return result; 
}