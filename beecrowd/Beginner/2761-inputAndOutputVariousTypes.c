// 2761-inputAndOutputVariousTypes.c
// Problem: Input and Output of Various Types
// Link: https://judge.beecrowd.com/en/problems/view/2761
// Solved on: 2024-09-10

#include <stdio.h>

int main() {
    int A;
    float B;
    char C;
    char D[51];

    scanf("%d %f %c %[^\n]", &A, &B, &C, D);

    printf("%d%.6f%c%s\n", A, B, C, D);
    printf("%d\t%.6f\t%c\t%s\n", A, B, C, D);
    printf("%10d%10.6f%10c%10.50s\n", A, B, C, D);

    return 0;
}
