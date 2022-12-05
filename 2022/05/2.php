<?php

$data = file_get_contents('input');
list($header, $moves) = explode("\n\n", $data);

$rows = array_slice(explode("\n", $header), 0, -1);
$elms = array_map(  // Parse the input in this god-forsaken language
    function($c) {
        return array_map(function($d) { return $d[1]; }, str_split($c, 4));
    },
    array_reverse($rows)
);

$stacks = array_map(null, ...$elms);  // Transpose - list of rows to list of stacks
$stacks = array_map(  // Just remove all spaces from the nested list
    function($c) { return array_filter($c, function($e) { return $e != " "; }); },
    $stacks
);

$movearr = array_slice(explode("\n", $moves), 0, -1);
foreach ($movearr as $move) {
    list($_, $n, $_, $from, $_, $to) = explode(" ", $move);
    // love my weak typing
    $el = array_splice($stacks[$from-1], -$n);
    array_push($stacks[$to-1], ...$el);
}
print(implode(array_map("end", $stacks)) . "\n");
