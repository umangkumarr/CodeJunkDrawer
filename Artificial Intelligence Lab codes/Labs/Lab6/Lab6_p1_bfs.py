import numpy as np
import random


class MultiAgentBfs:

    def __init__(self, pos, world, row, col, n):
        self.depth = np.zeros(n)
        self.row = row
        self.col = col
        self.agentPos = pos
        self.world = world
        self.n = n
        self.initalise()
        self.totalRewardsLeft = (world == 3).sum()
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]

        self.simulate()

    def getDirection(self, frm, to):
        if frm == [-1, -1]:
            return ''

        X = to[0] - frm[0]
        Y = to[1] - frm[1]

        if X == 0:
            if Y == 1:
                return 'R'
            else:
                return 'L'
        else:
            if X == 1:
                return 'D'
            else:
                return 'U'

    def initalise(self):
        self.queue = []
        for i in range(self.n):
            self.queue.append([[[[-1, -1], self.agentPos[i]]]])

        self.actions = []
        for i in range(self.n):
            self.actions.append([])

        self.vis = []
        for i in range(self.n):
            self.vis.append(np.zeros((self.row, self.col)))

        self.score = np.zeros(self.n)

        # print(self.vis)

    def isReward(self, pos):
        if(self.world[pos[0]][pos[1]] == 3):
            return True

        return False

    def isValidMove(self, x, y):
        if x >= 0 and y >= 0 and x < self.row and y < self.col:
            return True

        return False

    def moveAgent(self, agent):

        # if all the nodes are visited at depth i, then increment depth
        # print(self.queue[agent], self.totalRewardsLeft)
        if len(self.queue[agent][int(self.depth[agent])]) == 0:
            # print("hello\n")
            self.depth[agent] += 1
            self.moveAgent(agent)
            return

        rewards = []

        # find no of rewards nodes
        # for i in self.queue[agent][int(self.depth[agent])]:
        #     if self.isReward(i[1]):
        #         rewards.append(i)

        curNode = []

        if len(rewards):
            # pick random from rewards
            curNode = rewards[random.randrange(len(rewards))]
        else:
            # pick from non-reward Nodes
            l = len(self.queue[agent][int(self.depth[agent])])
            curNode = self.queue[agent][int(
                self.depth[agent])][random.randrange(l)]

        # remove the curNode from the queue
        self.queue[agent][int(self.depth[agent])].remove(curNode)

        # append actions
        self.actions[agent].append(self.getDirection(curNode[0], curNode[1]))
        # if curNode in rewards:
        if self.isReward(curNode[1]):
            self.actions[agent].append('S')
            self.totalRewardsLeft -= 1
            self.score[agent] += 1

        for i in range(4):
            x = curNode[1][0] + self.dx[i]
            y = curNode[1][1] + self.dy[i]

            if self.isValidMove(x, y) and self.vis[agent][x][y] == 0:
                if len(self.queue[agent]) - 1 <= self.depth[agent]:
                    self.queue[agent].append([])

                # print(self.queue)
                self.queue[agent][int(self.depth[agent]) +
                                  1].append([curNode[1], [x, y]])
                self.vis[agent][x][y] = 1

    def simulate(self):
        agent = 0
        while self.totalRewardsLeft:
            agent = agent % self.n
            self.moveAgent(agent)
            agent += 1

        # print(self.actions)
        # print(self.score)


if __name__ == "__main__":
    row, col = map(int, input().split())

    world = np.zeros((row, col), dtype=int)
    for i in range(row):
        world[i] = np.array(list(map(int, input().split(','))))

    for i in range(10):
        print(f'Round {i+1}')
        obj = MultiAgentBfs([[0, 0], [4, 3]], world, 5, 5, 2)
        res = []
        for j in range(len(obj.actions)):
            cnt = 0;
            for k in obj.actions[j]:
                if k == 'S':
                    cnt += 1
            print(f'Coins collected by agent {j+1} is {cnt}')
            res.append(cnt)
        
        if res[0] == res[1]:
            print("Match Draw")
        elif res[0] < res[1]:
            print(f"Agent Won:- {2}")
        else:
            print(f"Agent Won:- {1}")
        print()



