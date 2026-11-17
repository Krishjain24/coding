/* #include<iostream> 

int main(){
    std::cout<<"hey striver!!!\n"<<"hey raj!!!"<<std::endl;
    std:: cout<<"hey krish!!!";
    return 0;
}

#include<iostream> 
using namespace std;
int main(){
    int x,y;
    cin>>x>>y;
    cout<<"value of x:"<<x<<" value of y:"<<y<<endl;
    return 0;
}
/* to include all libraries we can use the following line */
#include<iostream>
using namespace std;

int factorial(int n){
    if (n==1 || n==0){
        return 1;
    }
    else{
        return n*factorial(n-1);
    }
}

int main(){
    int n;
    cin>>n;
    cout<<"factorial of "<<n<<" is "<<factorial(n)<<endl;
    return 0;
}