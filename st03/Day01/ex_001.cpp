// Exercise 1:
///////////////////////////////////////////////
// What will this program print on the console?

#include <iostream>
using namespace std;

int main()
{
    int a = 15;
    int b = 2;
    float x = 0.12;
    float y = 5.5;
    cout << a * b << endl;
    cout << x + y << endl;

    char c1 = 'a';
    char c2 = 'c';
    char c3 = 't';
    cout << c2 << c1 << c3 << endl;

    x = x + y;
    y = x + y;
    cout << x << ", " << y << endl;
}