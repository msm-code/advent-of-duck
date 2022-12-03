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

void update_counts(int *counts, char *text) {
    bool uniq[256] = {};
    while (*text) {
        if (uniq[*text]) {
            text++;
            continue;
        }
        uniq[*text] = true;
        counts[*text] += 1;
        text++;
    }
}

int main() {
    char rucksack1[0x1000];
    char rucksack2[0x1000];
    char rucksack3[0x1000];
    int total = 0;
    while (true) {
        int counts[256] = {};
        if (scanf("%s", rucksack1) <= 0) { break; }
        if (scanf("%s", rucksack2) <= 0) { break; }
        if (scanf("%s", rucksack3) <= 0) { break; }

        update_counts(counts, rucksack1);
        update_counts(counts, rucksack2);
        update_counts(counts, rucksack3);

        for (int i = 0; i < 256; i++) {
            if (counts[i] == 3){
                total += get_priority(i);
            }
        }
    }
    printf("%d\n", total);
    return 0;
}
