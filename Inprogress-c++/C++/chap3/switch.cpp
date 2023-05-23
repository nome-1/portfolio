#include <iostream>
#include <string>
using namespace std;

int main(){
    int number=5;
    switch (number)
    {
    case 1:
        cout <<"number is equal to 1";
        break;
    case 2:
        cout <<"number is equal to 2";
        break;
    
    default:
     cout <<"x did not match case";
        break;
    }
}