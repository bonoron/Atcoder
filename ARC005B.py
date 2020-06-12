import sys
from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt, ceil, floor
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
INF = float("inf")
sys.setrecursionlimit(10**7)

# 4近傍（右, 下, 左, 上）
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


def inside(y: int, x: int, H: int, W: int) -> bool: return 0 <= y < H and 0 <= x < W


def main():
    x, y, W = input().split()
    x, y = int(x) - 1, int(y) - 1
    field = []
    for _ in range(9):
        field.append(list(map(int, input())))

    # dy, dx
    d = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0), "RU": (-1, 1), "RD": (1, 1), "LU": (-1, -1), "LD": (1, -1)}

    ans = []
    for i in range(4):
        ans.append(field[y][x])
        ny, nx = y + d[W][0], x + d[W][1]
        if not inside(ny, nx, 9, 9):
            if y == 0:
                W = W.replace("U", "D")
            if y == 8:
                W = W.replace("D", "U")
            if x == 0:
                W = W.replace("L", "R")
            if x == 8:
                W = W.replace("R", "L")

            ny, nx = y + d[W][0], x + d[W][1]
        y, x = ny, nx

    print(*ans, sep="")


if __name__ == '__main__':
    main()