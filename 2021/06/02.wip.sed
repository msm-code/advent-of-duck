# Breed the fishes
s/^/_______________________________________________________________________________/g
s/,//g

:sort
s/1\([0-0]\)/\11/g
s/2\([0-1]\)/\12/g
s/3\([0-2]\)/\13/g
s/4\([0-3]\)/\14/g
s/5\([0-4]\)/\15/g
s/6\([0-5]\)/\16/g
s/7\([0-6]\)/\17/g
s/8\([0-7]\)/\18/g
t sort

:loop

# 1
s/0/9/g
s/1/0/g
s/2/1/g
s/3/2/g
s/4/3/g
s/5/4/g
s/6/5/g
s/7/6/g
s/8/7/g
t spawn1
:spawn1
s/9\([9JT0-5A-FK-Pa-fk-p]*\)\(.*\)$/\16\28/g
t spawn1

# 10
s/A/J/g
s/B/A/g
s/C/B/g
s/D/C/g
s/E/D/g
s/F/E/g
s/G/F/g
s/H/G/g
s/I/H/g
t spawn10
:spawn10
s/J\([9JT0-5A-FK-Pa-fk-p]*\)\([^8]*\)/\1G\2I/g
t spawn10

# 100
s/K/T/g
s/L/K/g
s/M/L/g
s/N/M/g
s/O/N/g
s/P/O/g
s/Q/P/g
s/R/Q/g
s/S/R/g
t spawn100
:spawn100
s/T\([9JT0-5A-FK-Pa-fk-p]*\)\([^8I]*\)/\1Q\2S/g
t spawn100

# 1000
s/a/j/g
s/b/a/g
s/c/b/g
s/d/c/g
s/e/d/g
s/f/e/g
s/g/f/g
s/h/g/g
s/i/h/g
t spawn1000
:spawn1000
s/j\([9JT0-5A-FK-Pa-fk-p]*\)\([^8IS]*\)/\1g\2i/g
t spawn1000

# 10000
s/k/t/g
s/l/k/g
s/m/l/g
s/n/m/g
s/o/n/g
s/p/o/g
s/q/p/g
s/r/q/g
s/s/r/g
t spawn10000
:spawn10000
s/t\([9JT0-5A-FK-Pa-fk-p]*\)\([^8ISi]*\)/\1q\2s/g
t spawn10000

# 1 -> 10
s/0000000000/A/g
s/1111111111/B/g
s/2222222222/C/g
s/3333333333/D/g
s/4444444444/E/g
s/5555555555/F/g
s/6666666666/G/g
s/7777777777/H/g
s/8888888888/I/g

# 10 -> 100
s/AAAAAAAAAA/K/g
s/BBBBBBBBBB/L/g
s/CCCCCCCCCC/M/g
s/DDDDDDDDDD/N/g
s/EEEEEEEEEE/O/g
s/FFFFFFFFFF/P/g
s/GGGGGGGGGG/Q/g
s/HHHHHHHHHH/R/g
s/IIIIIIIIII/S/g

# 100 -> 1000
s/KKKKKKKKKK/a/g
s/LLLLLLLLLL/b/g
s/MMMMMMMMMM/c/g
s/NNNNNNNNNN/d/g
s/OOOOOOOOOO/e/g
s/PPPPPPPPPP/f/g
s/QQQQQQQQQQ/g/g
s/RRRRRRRRRR/h/g
s/SSSSSSSSSS/i/g

# 1000 -> 10000
s/aaaaaaaaaa/k/g
s/bbbbbbbbbb/l/g
s/cccccccccc/m/g
s/dddddddddd/n/g
s/eeeeeeeeee/o/g
s/ffffffffff/p/g
s/gggggggggg/q/g
s/hhhhhhhhhh/r/g
s/iiiiiiiiii/s/g

t clean
:clean
s/_//
t loop
s/[k-s]/@/g
s/[a-i]/#/g
s/[K-S]/c/g
s/[A-J]/b/g
s/[0-9]/a/g
s/@/e/g
s/#/d/g

t sort2
:sort2
s/\([a-a]\)b/b\1/g
s/\([a-b]\)c/c\1/g
s/\([a-c]\)d/d\1/g
s/\([a-d]\)e/e\1/g
t sort2


# Count the resulting characters
# Original from https://www.gnu.org/software/sed/manual/html_node/sed-commands-list.html
# I guess this makes my code GPL.
#s/./a/g
H
x
s/\n//
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

