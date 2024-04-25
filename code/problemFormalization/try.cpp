#include <iostream>

using namespace std;


int main(){
    int a;
    char b;
    cout <<"a" << a << endl;
    cout <<"b" << b << endl;
    
    int * p;
    int ** c = &p;

    

    cout <<"unalocated ptr"<< p << endl;
    cout << "address cof ptr" << c << endl;

    p = new int();
    cout <<"allocated ptr" << p << endl;
    delete p;
    cout <<"deleted ptr"<< p << endl;

    return 0;
}