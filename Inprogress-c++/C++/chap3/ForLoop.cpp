#include <iostream>
#include <string>
using namespace std;

int main(){
    string t="aabbcc";
    for(int i =0; i<t.length();i++){
        cout<<t[i];
        for (int z = 0; z < t.length(); z++)
        {
           cout<<"you are lost";
        }
        
    }
}