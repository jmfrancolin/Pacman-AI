# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
# import pdb

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    visited_set = set()

    state = (problem.getStartState(), [])
    stack.push(state)

    while not stack.isEmpty():
        curr_node, path = stack.pop()

        if problem.isGoalState(curr_node):
            return path

        if curr_node not in visited_set:
            visited_set.add(curr_node)

            successors = problem.getSuccessors(curr_node)
            for candidate in successors:
                next_node = candidate[0]
                next_action = candidate[1]

                if next_node not in visited_set:
                    state = (next_node, path + [next_action])
                    stack.push(state)
                    # print stack
    return []

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    visited_set = set()

    state = (problem.getStartState(), [])
    queue.push(state)

    while not queue.isEmpty():
        curr_node, path = queue.pop()

        if problem.isGoalState(curr_node):
            return path

        if curr_node not in visited_set:
            visited_set.add(curr_node)

            successors = problem.getSuccessors(curr_node)
            for candidate in successors:
                next_node = candidate[0]
                next_action = candidate[1]

                if next_node not in visited_set:
                    state = (next_node, path + [next_action])
                    queue.push(state)
                    # print queue
    return []

def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue()
    visited_set = set()

    state = (problem.getStartState(), [], 0)
    priority = 0
    priority_queue.push(state, priority)

    while not priority_queue.isEmpty():
        curr_node, path, cost = priority_queue.pop()

        if problem.isGoalState(curr_node):
            return path

        if curr_node not in visited_set:
            visited_set.add(curr_node)

            successors = problem.getSuccessors(curr_node)
            for candidate in successors:
                next_node = candidate[0]
                next_action = candidate[1]
                action_cost = candidate[2]

                if next_node not in visited_set:
                    state = (next_node, path + [next_action], cost + action_cost)
                    priority = cost + action_cost
                    priority_queue.push(state, priority)
                    # print priority_queue
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue()
    visited_set = set()

    state = (problem.getStartState(), [], 0)
    priority = heuristic(problem.getStartState(), problem)
    priority_queue.push(state, priority)

    while not priority_queue.isEmpty():
        curr_node, path, cost = priority_queue.pop()

        if problem.isGoalState(curr_node):
            return path

        if curr_node not in visited_set:
            visited_set.add(curr_node)

            successors = problem.getSuccessors(curr_node)
            for candidate in successors:
                next_node = candidate[0]
                next_action = candidate[1]
                action_cost = candidate[2]

                if next_node not in visited_set:
                    state = (next_node, path + [next_action], cost + action_cost)
                    priority = cost + action_cost + heuristic(next_node, problem)
                    priority_queue.push(state, priority)
                    # print priority_queue
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
