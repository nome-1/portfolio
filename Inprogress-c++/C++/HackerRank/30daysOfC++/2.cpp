#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'solve' function below.
 *
 * The function accepts following parameters:
 *  1. DOUBLE meal_cost
 *  2. INTEGER tip_percent
 *  3. INTEGER tax_percent
 */

void solve(double meal_cost, int tip_percent, int tax_percent) {
   float tip=tip_percent/100.00*meal_cost;
   float tax=tax_percent/100.00*meal_cost;
   int meal=meal_cost+tax+tip;
   cout<< meal;

}
//10.25 17 5
int main()
{
    double meal_cost;
    cin>>meal_cost;

    int tip_percent;
    cin>>tip_percent;

    int tax_percent;
    cin>>tax_percent;

    solve(meal_cost, tip_percent, tax_percent);

    return 0;
}

