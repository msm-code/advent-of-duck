def charge!(x, y, map, flash)
    if (0...map.size) === y and (0...map[0].size) === x
        map[y][x] += 1
        if map[y][x] == 10
            flash.append([y, x])
        end
    end
end

def update!(map)
    flash = []
    for y in 0...map.size
        for x in 0...map[0].size
            charge!(x, y, map, flash)        
        end
    end
    flashes = 0
    while flash != []
        flashes += 1
        y, x = flash.pop()
        for dy in -1..1
            for dx in -1..1
                charge!(x + dx, y + dy, map, flash)
            end
        end
    end
    for y in 0...map.size
        for x in 0...map[0].size
            if map[x][y] > 9
                map[x][y] = 0
            end
        end
    end
    flashes
end

raw = File.open("input").read
data = raw.split.map{|row| row.chars.map{|x| x.to_i}}

total = data.size * data[0].size
for i in 1...1000
    if update!(data) == total
        print(i)
        break
    end
end