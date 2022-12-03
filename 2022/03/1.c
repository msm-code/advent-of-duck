#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define panik(x) { puts(x); exit(1); }

int get_priority(char c) {
    if ('a' <= c && c <= 'z') {
        return c - 'a' + 1;
    } else if ('A' <= c && c <= 'Z') {
        return c - 'A' + 27;
    } else {
        panik("weird item but ok");
    }
}

int main() {
    char rucksack[0x1000];
    int total = 0;
    while (scanf("%s", rucksack) > 0) {
        int item_count = strlen(rucksack);
        int item_per_compartment = item_count / 2;
        const char *comp1 = rucksack;
        const char *comp2 = rucksack + item_per_compartment;
        bool counted[256] = {};
        for (int i = 0; i < item_per_compartment; i++) {
            for (int j = 0; j < item_per_compartment; j++) {
                if (comp1[i] == comp2[j]) {
                    char duplicate = comp1[i];
                    if (counted[duplicate]) {
                        continue;
                    }
                    counted[duplicate] = true;
                    total += get_priority(comp1[i]);
                }
            }
        }
    }
    printf("%d\n", total);
    return 0;
}
