#! /usr/bin/env nix-shell
#! nix-shell -i perl -p perl

use warnings;
use strict;
use feature qw(say);

open(FH, '<', 'input') or die $!;

my $result = 0;
while(<FH>){
    my @matches = $_ =~ /(\d)/g;
    $result += $matches[0] . $matches[-1];
}
say $result;

close(FH);
