from icecream import ic

from pacman import GameState
from collections import deque


def BFS_pellets(state: GameState) -> tuple[tuple[int, int], int]:
    pellets_grid = state.getFood()
    goal_posns = pellets_grid.asList()
    return BFS(state, goal_posns)


def BFS_ghosts(state: GameState) -> tuple[tuple[int, int], int]:
    ghost_posns = state.getGhostPositions()
    # ghost position can be a floating-point number
    # like 2.5 when the ghost is edible
    # it doesn't really matter where we're rounding
    rounded_posns = [(round(x), round(y)) for x, y in ghost_posns]
    return BFS(state, rounded_posns)


def BFS_capsules(state: GameState) -> tuple[tuple[int, int], int]:
    goal_posns = state.getCapsules()
    return BFS(state, goal_posns)


def BFS(gameState: GameState, goal_posns: list[tuple[int, int]])\
        -> tuple[tuple[int, int], int]:
    '''
    Given a list of target positions (be it pellets, ghosts or capsules),
    return the closest position and the distance to it
    computed using BFS.
    '''
    if not goal_posns:
        return ((0, 0), 0)

    walls_matrix = gameState.getWalls()
    pacman_pos = gameState.getPacmanPosition()

    # Dimensions of the matrix
    height, width = walls_matrix.height, walls_matrix.width

    # BFS queue of (pos_x, pos_y, dist) tuples,
    # initialized with the pacman position
    queue: deque[tuple[int, int, int]] = deque(
        [(pacman_pos[0], pacman_pos[1], 0)])
    # Start with pacman position visited
    visited = {pacman_pos}

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) in goal_posns:
            return (x, y), dist
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            # check that new pos is within bounds
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            # check that new pos is not a wall
            if walls_matrix[nx][ny]:
                continue
            # check that pos has not been visited already

            if (nx, ny) in visited:
                continue
            queue.append((nx, ny, dist + 1))
            visited.add((nx, ny))

    return None  # No pellet found
