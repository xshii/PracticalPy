// pulls in the Python API 
//#include <Python.h>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <math.h>
#define N 6000  
#define M 10000
int main(void)
{
    srand(time(NULL));
    int k_list[] = {64, 80, 96, 104, 112, 120, 128, 144, 160, 176, 192, 200, 208, 224, 240, 256, 384};
    long unsigned length = sizeof(k_list)/sizeof(k_list[0]);

    int A[M][N];    // not able to generate such a bid matrix.
    
    for(int i=0;i<length;i++){
        printf("%d",i);
    }
    return 1;
}
long c_get_gflops(int m, int n, int k){
    return m*n*(2.0*k-1.0) / pow(1000.0,3);
}  
