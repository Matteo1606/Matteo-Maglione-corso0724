#include <stdio.h>

int main()
{
    int primo;
    int secondo;
    float media;

    printf("\nInserisci primo numero:");
    scanf("%d", &primo);

    printf("\nInserisci secondo numero:");
    scanf("%d", &secondo);

    media = (primo + secondo) /2;

    printf("\n (%d + %d) /2 = %.2f\n", primo, secondo, media);
    return 0;
}