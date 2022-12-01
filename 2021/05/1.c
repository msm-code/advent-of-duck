#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>
#define SWAP(X, Y) (X ^= Y ^= X ^= Y)

uint8_t ocean[1024][1024];

int main() {
    while (true) {
        int x1, y1, x2, y2;
        if (scanf("%d,%d -> %d,%d", &x1, &y1, &x2, &y2) < 0) break;

        if (x1 == x2) {
            if (y1 > y2) { SWAP(y1, y2); }
            while(y1 <= y2) ocean[x1][y1++]++;
        } else if (y1 == y2) {
            if (x1 > x2) { SWAP(x1, x2); }
            while(x1 <= x2) ocean[x1++][y1]++;
        }
    }
    int total = 0;
    for (int x = 0; x < 1024; x++) for (int y = 0; y < 1024; y++) total += ocean[x][y] > 1;
    printf("%d\n", total);
}
