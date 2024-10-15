# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

from typing import Any
from util import manhattanDistance
from game import Directions
import random
import util
import sys
import math
from icecream import ic

from pacman import GameState
from game import Agent, Actions
from search import BFS_ghosts, BFS_pellets, BFS_capsules, Astar_ghosts


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(
            gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(
            len(scores)) if scores[index] == bestScore]
        # Pick randomly among the best
        chosenIndex = random.choice(bestIndices)

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()      # Pacman position after moving
        newFood = successorGameState.getFood()               # Remaining food
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [
            ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        listFood = newFood.asList()                        # All remaining food as list
        ghostPos = successorGameState.getGhostPositions()  # Get the ghost position
        # Initialize with list
        mFoodDist = []
        mGhostDist = []

        # Find the distance of all the foods to the pacman
        for food in listFood:
            mFoodDist.append(manhattanDistance(food, newPos))

        # Find the distance of all the ghost to the pacman
        for ghost in ghostPos:
            mGhostDist.append(manhattanDistance(ghost, newPos))

        if currentGameState.getPacmanPosition() == newPos:
            return (-(float("inf")))

        for ghostDistance in mGhostDist:
            if ghostDistance < 2:
                return (-(float("inf")))

        if len(mFoodDist) == 0:
            return float("inf")
        else:
            minFoodDist = min(mFoodDist)
            maxFoodDist = max(mFoodDist)

        return 1000 / sum(mFoodDist) + 10000 / len(mFoodDist)


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """

    """
        Your improved evaluation function here
    """

    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


def minimax(node, depth: int, player,
            is_terminal, state_value, get_next_player,
            is_maximizing_player, get_children,
            alpha=None, beta=None, heuristic=None) \
        -> tuple[Any, int]:
    '''A general Minimax algorithm for a game of 2 teams.
    Players can take turns in any order, specified by the `get_nextplayer` function.
    Returns a tuple `(action, value)`, where action can be anything.
    `depth` denotes the total depth of the tree.

    If alpha and beta are not None, perform alpha-beta pruning.
    When doing alpha-beta pruning, a heuristic can be provided
    to order the children nodes such that the best branches are examined first.

    For pacman:
    - The first team consists only of Pacman, which is the maximizing player,
    and the second is the team of ghosts.
    - The nodes are GameState instances,
    - actions are Action instances (4 moves + stopping),
    - players are represented by agentIds, which in turn are integers.

    '''
    if depth == 0 or is_terminal(node):
        return (None, state_value(node))

    # if `white` is True, this is a turn of the maxizing team.
    # By convention, we root for the whites.
    whites = is_maximizing_player(player)
    value = -999999 if whites else 999999
    best_actions = []

    # use the heuristic to order the children
    # to improve alpha-beta pruning by examining best branches first
    unordered_children = get_children(node, player)
    if heuristic:
        children = sorted(
            unordered_children, key=lambda c: heuristic(c[1]), reverse=True)
    else:
        children = unordered_children

    for action, child in children:
        next_player = get_next_player(player)
        act, new_val = minimax(child, depth - 1, next_player,
                               is_terminal, state_value, get_next_player,
                               is_maximizing_player, get_children,
                               alpha=alpha, beta=beta)
        if (whites and new_val > value) or (not whites and new_val < value):
            value = new_val
            best_actions = [action]
            if alpha and beta:  # do pruning if alpha and beta are not None
                if whites:
                    alpha = max(alpha, value)
                    if value >= beta:
                        break
                else:
                    beta = min(beta, value)
                    if value <= alpha:
                        break
        elif new_val == value:
            best_actions.append(action)

    # pick a random action from the equally best ones
    # so that the player doesn't run in circles
    action = random.choice(best_actions)
    return (action, value)


def pacman_minimax(gameState: GameState, depth: int, eval_func, pruning=False) -> tuple[Any, int]:
    '''A wrapper around the general minimax for the pacman state.'''
    def is_pacman(p): return p == 0

    def next_states(state: GameState, agent_id: int) -> list[tuple[Actions, GameState]]:
        actions = state.getLegalActions(agent_id)
        next_states = [state.generateSuccessor(
            agent_id, a) for a in actions]
        return list(zip(actions, next_states))

    def next_agent(agent_id: int) -> int:
        agents = gameState.getNumAgents()
        return (agent_id + 1) % agents

    def is_terminal(state: GameState) -> bool:
        # pacman available actions:
        actionList = state.getLegalActions(0)
        return len(actionList) == 0 or state.isWin() or state.isLose()

    first_agent = 0  # pacman moves first

    if not pruning:
        result = minimax(gameState, depth, first_agent,
                         is_terminal, eval_func,
                         next_agent, is_pacman, next_states)
    else:
        def heuristic(state): return state.getScore()
        result = minimax(gameState, depth, first_agent,
                         is_terminal, eval_func,
                         next_agent, is_pacman, next_states,
                         alpha=-999999, beta=999999)

    return result


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """

        # the pacman CLI considers 1 depth level when every agent made 1 turn,
        # whereas the minimax algo. considers it as a single turn by one agent
        agents_count = gameState.getNumAgents()
        depth = self.depth * agents_count

        action, value = pacman_minimax(
            gameState, depth, self.evaluationFunction)
        return action


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Here is the place to define your Alpha-Beta Pruning Algorithm
    """

    def getAction(self, gameState):
        # the pacman CLI considers 1 depth level when every agent made 1 turn,
        # whereas the minimax algo. considers it as a single turn by one agent
        agents_count = gameState.getNumAgents()
        depth = self.depth * agents_count

        action, value = pacman_minimax(
            gameState, depth, self.evaluationFunction, pruning=True)
        return action


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    pacmanPos = currentGameState.getPacmanPosition()
    ghostList = currentGameState.getGhostStates()
    foods = currentGameState.getFood()
    capsules = currentGameState.getCapsules()
    # Return based on game state
    if currentGameState.isWin():
        return float("inf")
    if currentGameState.isLose():
        return float("-inf")
    # Populate foodDistList and find minFoodDist
    foodDistList = []
    for each in foods.asList():
        foodDistList = foodDistList + [util.manhattanDistance(each, pacmanPos)]
    minFoodDist = min(foodDistList)
    # Populate ghostDistList and scaredGhostDistList, find minGhostDist and minScaredGhostDist
    ghostDistList = []
    scaredGhostDistList = []
    for each in ghostList:
        if each.scaredTimer == 0:
            ghostDistList = ghostDistList + \
                [util.manhattanDistance(pacmanPos, each.getPosition())]
        elif each.scaredTimer > 0:
            scaredGhostDistList = scaredGhostDistList + \
                [util.manhattanDistance(pacmanPos, each.getPosition())]
    minGhostDist = -1
    if len(ghostDistList) > 0:
        minGhostDist = min(ghostDistList)
    minScaredGhostDist = -1
    if len(scaredGhostDistList) > 0:
        minScaredGhostDist = min(scaredGhostDistList)
    # Evaluate score
    score = scoreEvaluationFunction(currentGameState)
    """
        Your improved evaluation here
    """
    return score


# Abbreviation
better = betterEvaluationFunction


def dumbEvalFunc(state: GameState):
    '''
    As stated in the lab, task 1:
    score = - pellet_score + ghost_danger, where
    - pellet_score: min dist. to food
    - ghost_danger: min dist. to ghost
    '''
    closest_pellet_dist = BFS_pellets(state)[1]
    closest_ghost_dist = BFS_ghosts(state)[1]

    # the farther away, the worse;
    pellet_score = - closest_pellet_dist
    # the farther, the better
    ghost_score = closest_ghost_dist

    score = pellet_score + ghost_score
    return score


dumb = dumbEvalFunc


def dumb2EvalFunc(state: GameState, Astar=False):
    """
    Integrate the game's score with the distance to closest food.
    """
    # Maximum distance possible between any two points in the maze.
    # I don't think it matters if it's excessively big on the results,
    # but it will make the coefficients wildly different
    MAX_DIST = 100

    # force pacman to eat the pellet once he gets to it,
    # otherwise he won't eat the pellet because
    # closest_pellet_dist would jump from 1 to ~15
    # which would discourage him greatly.
    closest_pellet_dist = BFS_pellets(state)[1]
    pellet_count = state.getFood().count()
    # The less food remains, the better, therefore negative coeff.
    # The less distance the better, therefore negative coeff.
    # We multiply the pellet count by the max. possible dist,
    # such that eating a pellet is always better than having a pellet close by
    pellet_score = - closest_pellet_dist + MAX_DIST * (- pellet_count + 1)

    if not Astar:
        closest_ghost_dist = BFS_ghosts(state)[1]
    else:
        closest_ghost_dist = Astar_ghosts(state)[1]
    # the farther, the better
    ghost_score = closest_ghost_dist

    # eat ghosts!
    game_score = state.getScore()

    score = 10 * game_score + 2 * pellet_score + ghost_score
    return score


dumb2 = dumb2EvalFunc
def dumbAstar(s): return dumb2EvalFunc(s, True)
