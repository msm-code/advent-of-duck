#include <iostream>
#include <vector>
#include <tuple>

using Vec = std::tuple<int, int>;
using Board = std::vector<std::string>;

int height(const Board &board, int x, int y) {
    char raw = board[x][y];
    if (raw == 'S') { raw = 'a'; }
    if (raw == 'E') { raw = 'z'; }
    return raw - 'z';
}

Board parse() {
    Board lines;
    std::string line;
    while (std::getline(std::cin, line)) {
        lines.emplace_back(line);
    }
    return lines;
}

Vec find(const Board &board, char c) {
    for (int x = 0; x < board.size(); x++) {
        for (int y = 0; y < board[x].size(); y++) {
            if (board[x][y] == c) {
                return {x, y};
            }
        }
    }
    return {0, 0};
}

std::vector<Vec> neighbours(const Board &board, Vec pos) {
    auto [x, y] = pos;
    std::vector<Vec> out;
    if (x > 0) { out.push_back({x-1, y}); }
    if (x < board.size() - 1) { out.push_back({x+1, y}); }
    if (y > 0) { out.push_back({x, y-1}); }
    if (y < board[0].size() - 1) { out.push_back({x, y+1}); }
    return out;
}

int main() {
    Board board = parse();
    constexpr int INFINITY = 100000;
    std::vector<std::vector<int>> dist(board.size(), std::vector<int>(board[0].size(), INFINITY));
    auto [sx, sy] = find(board, 'E');
    std::vector<Vec> queue = {{sx, sy}};
    dist[sx][sy] = 0;
    for (int i = 0; i < queue.size(); i++) {
        auto [ex, ey] = queue[i];
        for (auto [nx, ny]: neighbours(board, queue[i])) {
            if (dist[nx][ny] != INFINITY) {
                continue;
            } else if (height(board, nx, ny) < height(board, ex, ey) - 1) {
                continue;
            } else if (board[nx][ny] == 'S' || board[nx][ny] == 'a') {
                std::cout << (dist[ex][ey] + 1) << std::endl;
                return 0;
            } else {
                dist[nx][ny] = std::min(dist[nx][ny], dist[ex][ey] + 1);
                queue.push_back({nx, ny});
            }
        }
    }
}
