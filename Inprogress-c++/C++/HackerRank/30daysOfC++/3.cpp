#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    int N;
    cin>>N;
    int b=2;
    if (N % b==1){
        cout<<"Weird";
    }
    else if(N % b==0 && 5>=N && N>2){
        cout<<"Not Weird";
    }
    else if (N % b==0 && 20>=N && N>6){
        cout<<"Weird";
    }
    else if( N >=20){
        cout<<"Not Weird";
    }
    return 0;
}