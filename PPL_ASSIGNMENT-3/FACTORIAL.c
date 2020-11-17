#include<stdio.h>

int find_factorial(int x) {
        if(x == 0 || x == 1){
            return 1;
        }
        else{
            return x*find_factorial(x-1);
        }
    }

int main() {

    int n=0;

    printf("Enter a Number : ");
    scanf("%d",&n);
    printf("Factorial of %d is %d\n",n, find_factorial(n));
    
    return 0;

}