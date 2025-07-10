// Exercise 3:
///////////////////////////////////////////////
// What will this program print on the console?

#include <iostream>
using namespace std;

int main()
{
    int a = 2;
    int b = 3;
    int c = 5;
    a = b + c;
    b = a % 4;
    b = b * 3;
    c = (a - b) * c;
    cout << a + b + c << endl;
    int someInt = a - b - c;
    b = someInt * someInt;
    cout << -b << endl;
}