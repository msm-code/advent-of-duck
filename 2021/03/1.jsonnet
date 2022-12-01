local nonempty = function(n) n != "";
local getn = function(n) function(arr) arr[n];
local parseBinary = function(num, acc)
    if num == "" then acc
    else parseBinary(num[1:], (acc * 2) + std.parseInt(num[0]));
local transpose = function(arr) [
    std.map(getn(i), arr)
    for i in std.range(0, std.length(arr[0]) - 1)
];
local bitwiseSelect = function(p, arr) std.map(p, transpose(arr));
local select = function(p, arr) parseBinary(std.join("", bitwiseSelect(p, arr)), 0);

local words = std.filter(nonempty, std.split(importstr "input", "\n"));
local gamma = function(arr) if std.count(arr, '1') > std.count(arr, '0') then '1' else '0';
local epsilon = function(arr) if std.count(arr, '1') > std.count(arr, '0') then '0' else '1';

select(gamma, words) * select(epsilon, words)
