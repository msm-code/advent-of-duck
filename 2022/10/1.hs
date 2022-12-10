apply ("noop":xs) = [0]
apply ("addx":num:xs) = [0, read num]
parse = scanl (+) 1 . concat . map apply . map words . lines
cycles = [20, 60, 100, 140, 180, 220]
eval rawcmds = print $ sum $ map (\x -> (x * (rawcmds!!(x-1)))) cycles
main = readFile "input" >>= (eval . parse)
