# Breed the fishes
s/^/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/g
:loop
s/0/n/g
s/1/0/g
s/2/1/g
s/3/2/g
s/4/3/g
s/5/4/g
s/6/5/g
s/7/6/g
s/8/7/g
s/n/8,6/g
t clean
:clean
s/a//
t loop
s/[^,]//g

# Count the resulting characters
# Original from https://www.gnu.org/software/sed/manual/html_node/sed-commands-list.html
# I guess this makes my code GPL.
s/./a/g
H
x
s/\n/a/
# Do the carry.
t a
: a;  s/aaaaaaaaaa/b/g;
: b;  s/bbbbbbbbbb/c/g;
: c;  s/cccccccccc/d/g;
: d;  s/dddddddddd/e/g;
: e;  s/eeeeeeeeee/f/g;
: f;  s/ffffffffff/g/g;
: g;  s/gggggggggg/h/g;
: h;  s/hhhhhhhhhh//g
: done
$! {
  h
  b
}
# On the last line, convert back to decimal
:countloop
/a/! s/[b-h]*/&0/
s/aaaaaaaaa/9/
s/aaaaaaaa/8/
s/aaaaaaa/7/
s/aaaaaa/6/
s/aaaaa/5/
s/aaaa/4/
s/aaa/3/
s/aa/2/
s/a/1/
: next
y/bcdefgh/abcdefg/
/[a-h]/ b countloop

