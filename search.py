# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
import pdb

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).

  You do not need to change anything in this class, ever.
  """

  def startingState(self):
    """
    Returns the start state for the search problem
    """
    util.raiseNotDefined()

  def isGoal(self, state): #isGoal -> isGoal
    """
    state: Search state

    Returns True if and only if the state is a valid goal state
    """
    util.raiseNotDefined()

  def successorStates(self, state): #successorStates -> successorsOf
    """
    state: Search state
     For a given state, this should return a list of triples,
     (successor, action, stepCost), where 'successor' is a
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental
     cost of expanding to that successor
    """
    util.raiseNotDefined()

  def actionsCost(self, actions): #actionsCost -> actionsCost
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
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):

    from game import Directions
    directionTable = {'South': Directions.SOUTH, 'North': Directions.NORTH,
                      'West': Directions.WEST, 'East': Directions.EAST}

    # create a Stack to keep track of nodes we are going to explore
    myStack = util.Stack()

    done = set()  #to keep track or explored nodes

    startPoint = problem.startingState()

    #we will push in tuples (coordinates, pass) in the stack
    myStack.push((startPoint, []))

    while not myStack.isEmpty():
      nextNode = myStack.pop()
      coordinate = nextNode[0]
      newPass = nextNode[1]

      if problem.isGoal(coordinate):
          return newPass
      if coordinate not in done:
          done.add(coordinate)
          for k in problem.successorStates(coordinate):
              if k[0] not in done:
                  myStack.push((k[0], newPass + [directionTable[k[1]]]))




def breadthFirstSearch(problem):
  "*** YOUR CODE HERE ***"

  from game import Directions
  directionTable = {'South': Directions.SOUTH, 'North': Directions.NORTH,
                    'West': Directions.WEST, 'East': Directions.EAST}

  # create a Queue to keep track of nodes we are going to explore
  myQueue = util.Queue()

  done = set()  #to keep track or explored nodes

  startPoint = problem.startingState()

  #we will push tuples (coordinates, pass) in the stack
  myQueue.push((startPoint, []))

  while not myQueue.isEmpty():
    nextNode = myQueue.pop()
    coordinate = nextNode[0]
    newPass = nextNode[1]

    if problem.isGoal(coordinate):
        return newPass
    if coordinate not in done:
        done.add(coordinate)
        for k in problem.successorStates(coordinate):
            if k[0] not in done:
                myQueue.push((k[0], newPass + [directionTable[k[1]]]))

def uniformCostSearch(problem):
    from game import Directions
    directionTable = {'South': Directions.SOUTH, 'North': Directions.NORTH,
                      'West': Directions.WEST, 'East': Directions.EAST}

    # create a Queue to keep track of nodes we are going to explore
    myQueue = util.PriorityQueue()

    done = set()  #to keep track or explored nodes

    startPoint = problem.startingState()

    #we will push in the queue tuples (coordinates, pass)
    #thus, we do not need additional dictionary for the passes (as we have in DFS)
    myQueue.push((startPoint, []), 0)

    while not myQueue.isEmpty():
      nextNode = myQueue.pop()
      coordinate = nextNode[0]
      newPass = nextNode[1]

      if problem.isGoal(coordinate):
          return newPass
      if coordinate not in done:
          done.add(coordinate)
          for k in problem.successorStates(coordinate):
              if k[0] not in done:
                  #we need to calculate a new priority
                  cost = problem.actionsCost(newPass + [directionTable[k[1]]])
                  myQueue.push((k[0], newPass + [directionTable[k[1]]]), cost)


def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0



def aStarSearch(problem, heuristic=nullHeuristic):
  from game import Directions
  directionTable = {'South': Directions.SOUTH, 'North': Directions.NORTH,
                    'West': Directions.WEST, 'East': Directions.EAST}

  # create a Queue to keep track of nodes we are going to explore
  myQueue = util.PriorityQueue()

  done = set()  #to keep track or explored nodes

  startPoint = problem.startingState()

  #we will push in the queue tuples (coordinates, pass)
  #thus, we do not need additional dictionary for the passes (as we have in DFS)
  myQueue.push((startPoint, []), 0)

  while not myQueue.isEmpty():
    nextNode = myQueue.pop()
    coordinate = nextNode[0]
    newPass = nextNode[1]

    if problem.isGoal(coordinate):
        return newPass
    if coordinate not in done:
        done.add(coordinate)
        for k in problem.successorStates(coordinate):
            if k[0] not in done:
                #we need to calculate a new priority
                cost = problem.actionsCost(newPass + [directionTable[k[1]]])
                myQueue.push((k[0], newPass + [directionTable[k[1]]]), cost + heuristic(k[0], problem))







# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch