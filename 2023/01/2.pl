#! /usr/bin/env nix-shell
#! nix-shell -i perl -p perl

use warnings;
use strict;
use feature qw(say);

open(FH, '<', 'input') or die $!;

my @replaces = (
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine",
);

my $result = 0;
while(<FH>){
    for my $i (1..9){
        my $x = $replaces[$i];
        $_ =~ s/$x/$x$i$x/g;
    }
    my @matches = $_ =~ /(\d)/g;
    $result += $matches[0] . $matches[-1];
}
say $result;

close(FH);
