import Text.ParserCombinators.Parsec
import Text.ParserCombinators.Parsec.Error
import Data.Maybe
import Data.List

data Tree = Tree [Tree] deriving Show

scoreChar :: Char -> Int
scoreChar ')' = 1
scoreChar ']' = 2
scoreChar '}' = 3
scoreChar '>' = 4

score :: [Char] -> Int
score = foldl ((+).(*5)) 0 . map scoreChar

missingChar :: Message -> Maybe Char
missingChar (Expect "\"}\"") = Just '}'
missingChar (Expect "\"]\"") = Just ']'
missingChar (Expect "\">\"") = Just '>'
missingChar (Expect "\")\"") = Just ')'
missingChar (SysUnExpect (x:xs)) = Just x
missingChar _ = Nothing

getMissing :: ParseError -> [Char]
getMissing = mapMaybe missingChar . errorMessages

bracket :: Char -> Char -> GenParser Char st Tree
bracket open close = do
    char open
    children <- many tree
    char close
    return $ Tree children

angle = bracket '<' '>'
curly = bracket '{' '}'
square = bracket '[' ']'
normal = bracket '(' ')'

tree :: GenParser Char st Tree
tree = normal <|> square <|> angle <|> curly

fullTree = do
    many tree
    eof 

-- just typecheck already
me sfx text e = if length ge /= 1 then "" else missing (sfx ++ ge) (text ++ ge)
    where ge = getMissing e

missing :: [Char] -> [Char] -> [Char]
missing sfx text = do
     let result = parse fullTree [] text
     either (me sfx text) (const sfx) result

middle l = l !! (length l `div` 2)

main = do
    file <- readFile "input"
    let missings = map (missing "") (lines file)
    let scores = filter (/= 0) $ map score missings
    putStrLn $ show $ middle $ sort scores