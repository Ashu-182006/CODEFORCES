#include <stdio.h>

int main() {
    int rows = 4;  // You can change this value for a bigger triangle
    int i, j, space;

    for(i = 0; i < rows; i++) {
        // Print spaces
        for(space = 0; space < rows - i - 1; space++) {
            printf(" ");
        }
        // Print stars
        for(j = 0; j < 2 * i + 1; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}