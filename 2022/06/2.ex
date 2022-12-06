data = String.graphemes(String.replace(File.read!("input"), "\n", ""))
tokens = for i <- 0..length(data)-4, do: Enum.slice(data, i, 14)
ndx = Enum.find_index(tokens, fn t -> Enum.uniq(t) == t end)
IO.puts(ndx + 14)

