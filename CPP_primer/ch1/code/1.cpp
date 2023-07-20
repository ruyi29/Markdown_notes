#include<iostream>
#include"Sales_item.h"
using namespace std;

int main()
{
    Sales_item books,book;
    cin>>books;
    while(cin>>book){
        if(books.isbn()==book.isbn()) books+=book;
        else{
            cout<<books<<endl;
            books=book;
        }
    }
    cout<<books;
    return 0;
}