with builtins;
with import <nixpkgs> {};
with lib.strings; let
  fileData = readFile ./input;
  fileLines = filter (l: l != "") (splitString "\n" fileData);
  parseRange = range: map toInt (splitString "-" range);
  parseLine = line: map parseRange (splitString "," line);
  inData = map parseLine fileLines;
  evaluatePair = x: let
    l0 = elemAt (elemAt x 0) 0;
    r0 = elemAt (elemAt x 0) 1;
    l1 = elemAt (elemAt x 1) 0;
    r1 = elemAt (elemAt x 1) 1;
  in
    if l0 >= l1 && r0 <= r1
    then 1
    else if l1 >= l0 && r1 <= r0
    then 1
    else 0;
  sum = l: lib.lists.foldr (a: b: a + b) 0 l;
in
  sum (map evaluatePair inData)
