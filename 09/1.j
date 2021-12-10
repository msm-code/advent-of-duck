T =: 10&,@:}:
B =: ,&10@:}.
L =: T&.|:
R =: B&.|:
chonk =: +/@:;@:((<T)*(<B)*(<L)*(<R)*(+&1))
data =: 1!:1<'input'
input =: 100 100 $(a.i.;}:> LF splitstring data)-48
0!:1 'chonk input'