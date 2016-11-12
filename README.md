# Search-in-Pac-Man
It is an assignment for "CMPS140: Artificial Intelligence" - Winter 2016 class at University of California Santa Cruz. My goal was to implement some search functions to help Pac-Man to find paths through his maze world, both to reach a particular location and to collect food efficiently.

I implemented some functions at search.py and searchAgents.py. The others files were provided by professor Getoor. 

The base implementation can be run: 
python pacman.py -l bigMaze -z .5 -p GoWestAgent

In this implementation the Pac-Man always goes West.

I implemented the depth-first search (DFS) algorithm in the depthFirstSearch function in search.py. Using a Stack to keep the possible actions I wrote the graph search version of DFS, which avoids expanding any already visited states. 

python pacman.py -l mediumMaze -z .5 -p SearchAgent -z .5

![Mockup for feature A](https://github.com/Katy-katy/PYTHON-Pac-Man-as-an-AI-Agent/blob/master/Screen_shot.png)

The Pac-Man board will show an overlay of the states explored, and the order in which they were explored (brighter red means earlier exploration). 
Path found with total cost of 130 actions
Search nodes expanded: 146

2.Then I  implemented the breadth-first search (BFS) algorithm in the breadthFirstSearch function in search.py. Using a Queue I wrote  a graph search algorithm that avoids expanding any already visited states.
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs -z .5

picture

Path found with total cost of 68 actions
Search nodes expanded: 269

Thus, BFD gives us a better solution, but it expands more nodes.


3. I Implemented the uniform-cost graph search algorithm using priority queue in the uniformCostSearch function in search.py. Now my Pac-Man choses the actions with the smallest cost. 

python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs -z .5

For the SearchAgent the result is the same as for BFS since the cost here is the number of steps taken.

4. I implemented  aStarSearch in search.py. A heuristic function (manhattanHeuristic in searchAgents.py) was provided. In this case, Pac-Man pays attention not just on the cost of the taken steps, but also on the remaining distance to the goal. It does not make big difference in the medium and big mazes since the Pac-Man has very few options to chose at every given points, but in the open maze, Pac-Man expands three times less nodes using AStarSearch

python pacman.py -l openMaze -p SearchAgent -a fn=ucs -z .5
Path found with total cost of 54 in 0.2 seconds
Search nodes expanded: 682

picture

python pacman.py -l openMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic  -z .5
Path found with total cost of 54 in 0.1 seconds
Search nodes expanded: 211


picture













pacman.py The main file that runs Pac-Man games. This file describes a Pac-Man GameState type.

game.py The logic behind how the Pac-Man world works. This file describes several supporting types like AgentState, Agent, Direction, and Grid.

util.py Useful data structures for implementing search algorithms.


graphicsDisplay.py	Graphics for Pac-Man
graphicsUtils.py	Support for Pac-Man graphics
textDisplay.py	ASCII graphics for Pac-Man
ghostAgents.py	Agents to control ghosts
keyboardAgents.py	Keyboard interfaces to control Pac-Man
layout.py	Code for reading layout files and storing their contents
