import sys
import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time
import copy
import random
import itertools
from collections import defaultdict
from queue import PriorityQueue
#input and output in file
sys.stdin = open('input.txt', 'r')
sys.stdout = open('out_advsearch.txt', 'w')


# directions to move
directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
h = 80  # height of blocks
indexes = [0, 1, 2, 3]


# dfs function on agent
def dfsOnAgent(agentMaze, dfsPath, agentStartState, coinCount, visitedMaze, n, m, emptyPath, maze, ep, dt):

    # dfs will run on maze
    x, y = agentStartState
    visitedMaze[x][y] = 1
    ep.append(agentStartState)
    # placeGreen(agentStartState)
    dfsPath.append(agentStartState)
    if(agentMaze[x][y] == 3):
        return (True, dfsPath)

    agentMaze[x][y] = 1

    # trying all directions
    for t in dt:
        a = int(x+directions[t][0])
        b = int(y+directions[t][1])
        newNode = (a, b)
        if(a >= 0 and b >= 0 and a < n and b < n and (newNode not in emptyPath) and (newNode not in ep) and (agentMaze[a][b] == 0 or agentMaze[a][b] == 3 or agentMaze[a][b] == 2)):
            #  print(newNode)
            res, path = dfsOnAgent(
                agentMaze, dfsPath, newNode, coinCount, visitedMaze, n, m, emptyPath, maze, ep, dt)
            if(res == True):
                return (True, path)

    agentMaze[x][y] = 0
    dfsPath.pop()
    nS = (x, y)
    # placeWhite(nS)
    return (False, dfsPath)


#  agent move function function
def moveAgent(agentNo, maze, n, m, startStates, vMazes, moves, collectedCoins, agentCount, coinCount, agentCoins, agentsVisitedPath, dt, noOfNodesVisited):

    if(len(collectedCoins) < coinCount):
        dfsPath = []
        agentMaze = copy.deepcopy(maze)
        vm = np.zeros((int(n), int(m)), dtype=int)
        emptyPath = []

    #    when coin found to any of agent
        if (maze[startStates[agentNo % agentCount][0]][startStates[agentNo % agentCount][1]] == 3):
            collectedCoins.append(startStates[agentNo % agentCount])
            agentCoins[agentNo % agentCount].append(
                startStates[agentNo % agentCount])
            maze[startStates[agentNo % agentCount][0]
                 ][startStates[agentNo % agentCount][1]] = 0
            emptyPath = []
            noOfNodesVisited[agentNo %
                             agentCount] += len(agentsVisitedPath[agentNo % agentCount])
            agentsVisitedPath[agentNo % agentCount] = []
        isCoin, pth = dfsOnAgent(agentMaze, dfsPath, startStates[agentNo % agentCount], coinCount, vm,
                                 n, m, agentsVisitedPath[agentNo % agentCount], maze, emptyPath, dt[agentNo % agentCount])
        agentsVisitedPath[agentNo % agentCount].append(
            startStates[agentNo % agentCount])

        if(len(dfsPath) > 1):
            startStates[agentNo % agentCount] = dfsPath[1]
        else:
            agentsVisitedPath[agentNo % agentCount] = []

        #  again moving next agent
        moveAgent((agentNo+1), maze, n, m, startStates, vMazes, moves, collectedCoins,
                  agentCount, coinCount, agentCoins, agentsVisitedPath, dt, noOfNodesVisited)
    else:

        # Deciding each round winner
        totalNodesExplored = np.zeros(int(agentCount), dtype=int)

        def func():
            return 0
        scoreDict2 = defaultdict(func)
        scoreDict = {}

        for i in range(0, agentCount):
            scoreDict[i] = len(agentCoins[i])
            scoreDict2[len(agentCoins[i])] = scoreDict2[len(agentCoins[i])]+1
            print("Coins Collected by agent", i+1, "is", len(agentCoins[i]))
            totalNodesExplored[i] += noOfNodesVisited[i]+1
            #    print(noOfNodesVisited[i])

        print("Total Nodes Explored:", totalNodesExplored)
        maxScore = 0
        ag = -1

        for i in scoreDict:
            if(scoreDict[i] > maxScore):
                maxScore = max(scoreDict[i], maxScore)
                ag = i

        if(scoreDict2[maxScore] > 1):
            print("Match Draw")
        else:
            print("Agent Won:-", ag+1)

        print("")


# starting all agent
def agentFunction(maze, n, m, startStates, agentCount, coinCount, dt, totalAgentCoins):

    vMazes = []
    collectedCoins = []
    agentCoins = []
    agentsVisitedPath = []
    noOfNodesVisited = np.zeros(int(agentCount), dtype=int)
    for i in range(0, agentCount):
        visitedMaze = np.zeros((int(n), int(m)), dtype=int)
        vMazes.append(visitedMaze)
        agentCoins.append([])
        agentsVisitedPath.append([])
        #  noOfNodesVisited.append([])
    moves = random.sample(list(itertools.permutations(indexes)), (agentCount))
    agentNo = 0
    moveAgent(agentNo, maze, n, m, startStates, vMazes, moves, collectedCoins,
              agentCount, coinCount, agentCoins, agentsVisitedPath, dt, noOfNodesVisited)
    for i in range(0, agentCount):
        totalAgentCoins[i] += (agentCoins[i])


# main driver function
def driverFunction():

    n = 5    # height
    m = 5    # width
    maze = np.zeros((int(n), int(m)), dtype=int)
    startStates = []
    coinCount = 0
    # maze formation
    for i in range(0, n):
        a = input().split(',')
        for j in range(0, m):
            if(int(a[j]) == 2):
                startStates.append((i, j))

            else:
                maze[i][j] = int(a[j])
                if(int(a[j]) == 3):
                    coinCount += 1

    # no of times two agent will run
    testcases = int(input())
    scoreListAgent = []
    totalAgentCoins = []
    for s in startStates:
        scoreListAgent.append([])
        totalAgentCoins.append([])

    # randomized direction on move of each agent
    dt = random.sample(list(itertools.permutations(indexes)), 1)
    round = 0
    while(testcases > 0):
        agentCount = len(startStates)
        round += 1
        print("Round", round)
        Mazes = copy.deepcopy(maze)
        dt = random.sample(list(itertools.permutations(indexes)), agentCount)
        # print(dt)
        agentFunction(Mazes, n, m, startStates, agentCount,
                      coinCount, dt, totalAgentCoins)
        # print("Next Agent")
        testcases -= 1

    # Deciding the final winner
    winner = -1
    maxC = 0

    def func():
        return 0
    scoreTotal = defaultdict(func)
    for tc in range(0, len(totalAgentCoins)):
        scoreTotal[len(totalAgentCoins[tc])] += 1
        if(len(totalAgentCoins[tc]) > maxC):
            maxC = len(totalAgentCoins[tc])
            winner = tc

    if(scoreTotal[maxC] > 1):
        print('Total Series Draw')
    else:
        print("Final Agent", winner+1, "Won With total coins", maxC)


driverFunction()
