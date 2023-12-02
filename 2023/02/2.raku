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
        make $<game>.map({ .made }).sum;
    }
    method game($/) {
        my %merged = $<reveal>.map(*.made).reduce(sub ($x, $y) {
            my $result = %($x);
            for %($y).kv -> $key, $value {
                $result{$key} = $result{$key} max $value;
            }
            $result
        });
        make [*] %merged.values;
    }
    method reveal($/) {
        make $<entry>.map(*.made);
    }
    method entry($/) {
        make ~$<color>=>+$<count>;
    }
});

say $x.made;
