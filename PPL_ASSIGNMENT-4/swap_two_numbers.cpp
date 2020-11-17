// C++ Program to illustrate Pass by Reference
#include<iostream>
using namespace std;

void swapNum(int &a, int &b) {
    int z = a;
    a=b;
    b=z;
}

int main() {

    int a=100;
    int b=900;

    cout << "Before Swapping : " << "a = " << a << ", b = " << b << endl;

    swapNum(a, b);

    cout << "After Swapping : " << "a = " << a << ", b = " << b << endl;

    return 0;
}