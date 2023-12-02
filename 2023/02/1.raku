#! /usr/bin/env nix-shell
#! nix-shell -i rakudo -p rakudo

grammar Parser {
    rule TOP { ^ <game>+ $ }
    rule game { 'Game' <id> ':' <reveal> [';' <reveal>]* }
    rule reveal { <entry> [',' <entry> ]*}
    rule entry { <count> <color> }
    rule count { \d+ }
    token color { 'red' | 'green' | 'blue' }
    rule id { \d+ }
}

my $text = slurp "input";
my $x = Parser.parse($text, actions => class {
    method TOP($/) {
        make $<game>.map({ $_<id> if .made }).sum;
    }
    method game($/) {
        make $<reveal>.map(*.made).all;
    }
    method reveal($/) {
        make $<entry>.map(*.made).all;
    }
    method entry($/) {
        my %max = <red 12 green 13 blue 14>;
        make $<count> <= %max{$<color>};
    }
});

say $x.made;
