#include<iostream>
using namespace std;

int main(){
    int a=1,b=2,*c=&a;
    c=&b;
    cout<<*c;
    return 0;
}