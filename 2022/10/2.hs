import Data.List
apply ("noop":xs) = [0]
apply ("addx":num:xs) = [0, read num]
isVisible h p = p >= (h-1) && p <= (h+1)
mapPixel p = if p then '#' else '.'
-- I just *REFUSE* to install split for something so simple as chunks
splitEvery n = takeWhile (not.null) . map (take n) . iterate (drop n)
heads = concat $ replicate 6 [0..39]
parse = scanl (+) 1 . concat . map apply . map words . lines
eval = unlines . splitEvery 40 . map mapPixel . zipWith isVisible heads
main = readFile "input" >>= putStrLn . (eval . parse)
