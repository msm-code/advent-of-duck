import Text.ParserCombinators.Parsec
import Text.ParserCombinators.Parsec.Error
import Debug.Trace
import Data.Maybe

data Tree = Tree [Tree] deriving Show

errorValue :: Message -> Maybe Int
errorValue (SysUnExpect "\")\"") = Just 3
errorValue (SysUnExpect "\"]\"") = Just 57
errorValue (SysUnExpect "\"}\"") = Just 1197
errorValue (SysUnExpect "\">\"") = Just 25137
errorValue _ = Nothing

value :: ParseError -> Int
value = last . (0:) . mapMaybe errorValue . errorMessages

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

main = do
    file <- readFile "input"
    let trees = map (parse tree []) (lines file)
    let errors = map (either value (const 0)) trees
    putStrLn $ show $ sum errors