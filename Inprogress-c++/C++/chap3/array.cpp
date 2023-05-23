#include <iostream>
#include <string>
using namespace std;

int main(){
   int nums[5]={1,2,3,4};
   int length=sizeof(nums)/sizeof(nums[0]);
   cout<<length<<'\n';
   cout<<nums;
}