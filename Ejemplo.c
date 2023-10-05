#include <stdio.h>

int main() {
    double num1, num2, suma;

    printf("Ingrese el primer número: ");
    scanf("%lf", &num1);

    printf("Ingrese el segundo número: ");
    scanf("%lf", &num2);

    suma = num1 + num2;

    printf("La suma es: %.2lf\n", suma);

    return 0;
}
