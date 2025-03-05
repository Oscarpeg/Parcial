#include <stdio.h>
#include <time.h>
#include <sys/resource.h> 

unsigned long long factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    return n * factorial(n - 1);
}

int main() {
    int num = 900;
    struct rusage usage;
    
    clock_t start = clock(); 

    unsigned long long resultado = factorial(num);

    clock_t end = clock(); 
    getrusage(RUSAGE_SELF, &usage); 

    printf("Factorial(%d) = %llu\n", num, resultado);
    printf("Tiempo de ejecución: %f segundos\n", (double)(end - start) / CLOCKS_PER_SEC);
    printf("Memoria usada: %ld KB\n", usage.ru_maxrss);

    return 0;
}
