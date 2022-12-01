{
    split($0, input, ",");
}
END {
    for (key in input) { counts[input[key]] += 1 }

    for (i = 0; i < 256; i++) {
        born = counts[0];
        counts[0] = counts[1];
        counts[1] = counts[2];
        counts[2] = counts[3];
        counts[3] = counts[4];
        counts[4] = counts[5];
        counts[5] = counts[6];
        counts[6] = counts[7];
        counts[7] = counts[8];
        counts[8] = born;
        counts[6] += born;
    }

    total = 0
    for (key in counts) { total += counts[key] }
    print total
}
