from __future__ import print_function
from icecream import ic
import matplotlib.pyplot as plt
from heapq import heappush, heappop

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


class AStarGraph(object):
    def __init__(self, walls: list[list[bool]], w: int, h: int):
        self.walls = walls
        self.w = w
        self.h = h

    def heuristic(self, start, goal):
        dx = abs(start[0] - goal[0])
        dy = abs(start[1] - goal[1])
        return dx + dy

    def get_vertex_neighbours(self, pos):
        n = []
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x2 = pos[0] + dx
            y2 = pos[1] + dy
            if x2 < 0 or x2 >= self.w or y2 < 0 or y2 >= self.h:
                continue
            if self.walls[x2][y2]:
                continue
            n.append((x2, y2))
        return n

    def move_cost(self, a, b):
        return 1  # Normal movement cost


def AStarSearch(start, end, graph, route=False):
    G = {}  # Actual movement cost to each position from the start position
    F = {}  # Estimated movement cost of start to end going via this position

    # Initialize starting values
    G[start] = 0
    F[start] = graph.heuristic(start, end)

    closedVertices = set()
    openVertices = [(F[start], start)]
    cameFrom = {}

    while len(openVertices) > 0:
        # Get the vertex in the open list with the lowest F score

        currentFscore, current = heappop(openVertices)

        # Check if we have reached the goal
        if current == end:
            if route:
                # Retrace our route backward
                path = [current]
                while current in cameFrom:
                    current = cameFrom[current]
                    path.append(current)
                path.reverse()
                return path, F[end]  # Done!
            else:
                return F[end]

        # Mark the current vertex as closed
        closedVertices.add(current)

        # Update scores for vertices near the current position
        for neighbour in graph.get_vertex_neighbours(current):
            if neighbour in closedVertices:
                continue  # We have already processed this node exhaustively
            candidateG = G[current] + graph.move_cost(current, neighbour)

            if G.get(neighbour) and candidateG >= G[neighbour]:
                continue  # This G score is worse than previously found

            # Adopt this G score
            cameFrom[neighbour] = current
            G[neighbour] = candidateG
            H = graph.heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H

            if neighbour not in (p[1] for p in openVertices):
                # Discovered a new vertex
                heappush(openVertices, (F[neighbour], neighbour))

    raise RuntimeError("A* failed to find a solution")


def Astar_ghosts(state: GameState) -> tuple[tuple[int, int], int]:
    ghost_floating_posns = state.getGhostPositions()
    # ghost position can be a floating-point number
    # like 2.5 when the ghost is edible
    # it doesn't really matter where we're rounding
    ghost_posns = [(round(x), round(y)) for x, y in ghost_floating_posns]

    walls_matrix = state.getWalls()
    height, width = walls_matrix.height, walls_matrix.width
    pacman_pos = state.getPacmanPosition()

    graph = AStarGraph(walls_matrix, width, height)
    ghost_dists = []
    for ghost_posn in ghost_posns:
        dist = AStarSearch(pacman_pos, ghost_posn, graph)
        ghost_dists.append((ghost_posn, dist))

    return min(ghost_dists, key=lambda r: r[1])


if __name__ == "__main__":
    walls = [(2, 4), (2, 5), (2, 6), (3, 6), (4, 6),
             (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (4, 2), (3, 2)]
    matrix = []
    for x in range(7):
        matrix.append([])
        for y in range(7):
            matrix[x].append(True if (x, y) in walls else False)
    ic(matrix)

    graph = AStarGraph(matrix, 7, 7)
    result, cost = AStarSearch((0, 0), (6, 6), graph, route=True)
    print("route", result)
    print("cost", cost)
    plt.plot([v[0] for v in result], [v[1] for v in result])
    plt.plot([v[0] for v in walls], [v[1] for v in walls])
    plt.xlim(-1, 8)
    plt.ylim(-1, 8)
    plt.show()
