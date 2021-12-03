local nonempty = function(n) n != "";
local getn = function(n) function(arr) arr[n];
local parseBinary = function(num, acc)
    if num == "" then acc
    else parseBinary(num[1:], (acc * 2) + std.parseInt(num[0]));
local bitwiseDescend = function(p, i, arr)
    local best = p(std.map(getn(i), arr));
    if std.length(arr) == 1 then arr[0]
    else bitwiseDescend(p, i+1, std.filter(function(elm) elm[i] == best, arr));
local descend = function(p, arr) parseBinary(bitwiseDescend(p, 0, arr), 0);

local words = std.filter(nonempty, std.split(importstr "input", "\n"));
local gamma = function(arr) if std.count(arr, '1') >= std.count(arr, '0') then '1' else '0';
local epsilon = function(arr) if std.count(arr, '1') >= std.count(arr, '0') then '0' else '1';

descend(gamma, words) * descend(epsilon, words)
