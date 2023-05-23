#include <iostream>
#include <string>
using namespace std;

int main(){
    string s="Hello World!";
    int len=s.size();
    char in=s[3];
    string sub=s.substr(0,5);
    string toga=in + sub;
    cout<< " length of "<< s << len;
    cout<<"\n"<<in<< sub<<"\n"<<toga;
}