//  2758-floatingNumber.c
//  Problem: Floating Number Input and Output
//  Link: https://judge.beecrowd.com/en/problems/view/2758
//  Solved on: 2024-09-10

#include <stdio.h>

void floatingNumber() {
    float a, b;
    double c, d;

    scanf("%f %f", &a, &b);
    scanf("%lf %lf", &c, &d);

    printf("A = %.6f, B = %.6f\n", a, b);
    printf("C = %.6lf, D = %.6lf\n", c, d);

    printf("A = %.1f, B = %.1f\n", a, b);
    printf("C = %.1lf, D = %.1lf\n", c, d);

    printf("A = %.2f, B = %.2f\n", a, b);
    printf("C = %.2lf, D = %.2lf\n", c, d);

    printf("A = %.3f, B = %.3f\n", a, b);
    printf("C = %.3lf, D = %.3lf\n", c, d);

    printf("A = %.3E, B = %.3E\n", a, b);
    printf("C = %.3E, D = %.3E\n", c, d);

    printf("A = %.0f, B = %.0f\n", a, b);
    printf("C = %.0lf, D = %.0lf\n", c, d);
}

int main() {
    floatingNumber();
    return 0;
}

