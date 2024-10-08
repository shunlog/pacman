from icecream import ic

from pacman import GameState
from collections import deque


def BFS(gameState: GameState, ghosts=False) -> tuple[tuple[int, int], int]:
    if not ghosts:
        pellets_grid = gameState.getFood()
        goal_posns = pellets_grid.asList()
    else:
        goal_posns = gameState.getGhostPositions()
        goal_posns = [(round(x), round(y)) for x, y in goal_posns]
    if not goal_posns:
        return ((0, 0), 0)

    walls_matrix = gameState.getWalls()
    pacman_pos = gameState.getPacmanPosition()

    # Dimensions of the matrix
    height, width = walls_matrix.height, walls_matrix.width

    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS queue initialized with the pacman position
    queue = deque([(pacman_pos[0], pacman_pos[1], 0)])  # (x, y, distance)
    # Start with pacman position visited
    visited = {pacman_pos}

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) in goal_posns:
            return (x, y), dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and not walls_matrix[nx][ny] and (nx, ny) not in visited:
                queue.append((nx, ny, dist + 1))
                visited.add((nx, ny))

    return None  # No pellet found
