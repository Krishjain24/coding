// LECTURE 2:-> VARIABLE, DATA TYPES, AND PSEUDOCODE

/* ; -> It is known as STATEMENT TERMINATOR .It is equivalent to full stop*/

// SOME IMP COMMAND OF TERMINAL 
/*here [] represent the name of cpp file
1.g++ [].cpp -o [] -> used to check whether the code is successfully compiled or not 
2. .\[].exe OR .\[] -> to run executable file 
3. ; -> to use 2 command in one line 
4. clear-> to clear terminal 
5."up arrow " -> to get prev command 

 */

// BOILERPLATE CODE
/*#include<iostream>
using namespace std;
 
int main(){
    // CODE

    return 0;
}*/

// COMMENTS:-> anything which is written in code but completely ignoer by compiler
/*  //-> for single line comment
    /*  -> for multi line comment 
    some important points about comment
    1. comment is used to explain the code 
    2. comment is used to make code more readable
    SHORTCUTS FOR COMMENT
    1. ctrl + / -> for single line comment
    2. shift + alt + A -> for multi line comment
*/

// VARIABLE:-> A variable is a name given to a memory location that stores data which can be changed during program execution   
/*
'' -> It is known as CHARACTER LITERAL .It is used to represent a single character in C++ 


//  identifiers:-> An identifier is a name given to a variable, function, class, or any other user-defined item in C++ .

// data types:-> A data type is a classification of data that tells the compiler or interpreter how the programmer intends to use the data.
It defines the type of data that can be stored in a variable or returned by a function.
 
1. int--> It is used to represent integer data type in C++ . it occupies 4 bytes of memory and can store whole numbers from -2,147,483,648 to 2,147,483,647
2. float--> It is used to represent floating-point data type in C++ .It can store decimal. it occupies 4 bytes of memory and can store numbers from 1.17549e-38 to 3.40282e+38
it take 7 digits of precision after decimal point and f in ending

3. bool--> It is used to represent boolean data type in C++ .It can store true or false value. it occupies 1 byte of memory for compiler true is 1 and false is 0

4. char--> It is used to represent character data type in C++ .It can store a single character . it occupies 1 byte of memory

*/

// TO CHECK THE SIZE OF DATA TYPE
/* we use sizeof() operator to check the size of data type in C++ . it returns the size of data type in bytes
eg- 
cout << "Size of int: " << sizeof(int) << " bytes" << endl;
cout << "Size of float: " << sizeof(float) << " bytes" << endl;
cout << "Size of bool: " << sizeof(bool) << " bytes" << endl;
cout << "Size of char: " << sizeof(char) << " bytes" << endl; 
every thing is stored in ascii value in memory . so we can use ascii value to check the size of data type in C++ . it returns the size of data type in bytes
*/

// TYPE CONVERSION AND TYPE CASTING:-> Type conversion is the process of converting one data type to another data type in C++ . it can be done in two ways
/*1.type conversion(Implicit):-> It is done by the compiler automatically . it is also called as automatic type conversion .
it is storing small value in big(eg- float to double)*/
/* eg- #include<iostream>
using namespace std;
 
int main(){
    char grade='A';
    int value= grade;
    cout<<value<<endl;
    return 0;
} */
/*2.type casting(explicit)-> it done manually by the programmer 
it is the processs of storing big value in small(eg-double to int )
/* */
/* #include<iostream>
using namespace std;
 
int main(){
    double price=100.99;
    int newPrice=(int)price;
    cout<<newPrice<<endl; 
    return 0;
} */

// INPUT IN C++
// use cin>> variable
/* #include<iostream>
using namespace std;
 
int main(){
    int age;
    cout<<age;
    return 0; // gives garbage value
} */
/* eg- #include<iostream>
using namespace std;
 
int main(){ 

    return 0;
} */