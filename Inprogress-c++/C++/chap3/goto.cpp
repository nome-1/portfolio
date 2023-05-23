#include <iostream>
#include <string>
using namespace std;

int main(){
   goto first;

   third:cout<<"third";return 0;
   second:cout<<"second"<<" ";goto third;
   first:cout<<"first"<<" ";goto second;
}