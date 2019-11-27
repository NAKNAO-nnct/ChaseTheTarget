from Maze import *
from Actor import *
import math
import copy
import numpy as np
import matplotlib.pyplot as plt


class Simulator:
    maze = None
    chre = None
    target = None

    def __init__(self, maze_conncet, chre_connect, target_conncet):
        self.maze = copy.deepcopy(maze_conncet)
        self.chre = copy.deepcopy(chre_connect)
        self.target = copy.deepcopy(target_conncet)

    # アクションを実行
    def doAction(self, action):
        before_reward = self.chre.reward.getReward()
        self.target.main()
        p = self.maze.moveRelative(self.chre.name, action + 5)
        if p is not 0:
            if self.chre.moveTo(p):
                maze.setActorPosition(self.chre.name, p)
                self.chre.searchTarget()
                return self.chre.reward.getReward() - before_reward
        # if self.chre.moveTo(9):
        self.chre.moveTo(9)
        self.maze.setActorPosition(self.chre.name, p)
        self.chre.searchTarget()
        return self.chre.reward.getReward() - before_reward
        # else:
        #     while True:
        #         p = self.maze.moveRelative(
        #             self.chre.name, random.randrange(5) + 5)
        #         if p is not 0:
        #             if self.chre.moveTo(9):
        #                 self.chre.searchTarget()
        #                 return self.chre.reward.getReward() - before_reward

    # 状態を取得
    def getState(self):
        return self.maze, self.chre, self.target


# 移動平均
def moveAverage(data, n):
    out = []
    for i in range(-int((n-1) / 2), len(data) - int((n-1) / 2)):
        for j in range(n):
            _tmp = 0
            if (i < 0):
                _tmp += data[j]
                out.append(_tmp)

    with open('./result.csv', mode='w') as f:
        for i in range(len(out)):
            f.write(str(out[i])+',')

    # plt.plot(np.array(len(out)), out, label="step")
    # plt.xlabel('episode/{}'.format(100))
    # plt.ylabel('max_step')
    # plt.show()


if __name__ == "__main__":
    from datetime import datetime as dt

    max_step = 10000

    out = []

    data = [
        0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
        0, 1, 1, 0, 0, 0, 1, 0, 0, 0,
        0, 1, 1, 0, 1, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0, 1, 0,
        0, 0, 0, 0, 1, 0, 0, 0, 1, 0,
        0, 1, 1, 0, 1, 0, 1, 1, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 1, 0, 1,
        0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
        0, 0, 0, 0, 1, 0, 0, 1, 0, 1,
        0, 0, 0, 0, 1, 0, 0, 0, 0, 1
    ]

    q = []
    bid = []

    for i in range(100):
        q.append([0, 0, 0, 0])
        bid.append([0, 0, 0, 0])
    x = 0
    while True:
        maze = Maze(data, int(math.sqrt(len(data))))

        chre = Chaser(maze, 'chaser')
        user = Target(maze, 'target')
        g_r = 0

        log = []

        for o in range(200):
            if maze.isEnd():
                out.append(g_r)
                # print(x, out[-1])
                break
            s = user.getPosition()
            r = []
            for i in range(4):
                bid[s][i] = 0.1 * q[s][i]
                simulator = Simulator(maze, chre, user)
                r.append(simulator.doAction(i))
                next_state = simulator.getState()
                s_dash = next_state[1].getPosition()
                next_bid = q[s_dash]
                r_dash = []
                for j in range(4):
                    r_dash.append(simulator.doAction(j))
                next_action = q[s_dash][r_dash.index(max(r_dash))]

                q[s][i] = q[s][i] + r[i] + next_action - bid[s][i]
                # print(q[s][i])

                # print(q[s].index(max(q[s]))+5)
                # for i in range(4):
            act_s = maze.moveRelative(
                chre.name, q[s].index(max(q[s])) + 5)
            # if act_s != chre.position:
            #     break

            g_r += max(r)
            # maze.setActorPosition(chre.name, act_s)
            chre.moveTo(act_s)
            print(q[s].index(max(q[s])) + 5, act_s)

            # if chre.position == act_s:
            #     chre.main()
            # else:
            #     chre.moveTo(act_s)
            # chre.main()
            user.main()
            chre.searchTarget()
            log.append([str(i), str(o), chre.position, user.position])
            # chre.main()

        if (x % 10 == 0):
            print(x)
            # print(q)
            tdatetime = dt.now()
            tstr = tdatetime.strftime('%Y%m%d_%H%M%S')
            with open('./log/{}.txt'.format(tstr), mode='w') as f:
                for i in log:
                    for j in i:
                        f.write(str(j) + ',')
                    f.write('\n')
        x += 1

        if x > max_step:
            break
    moveAverage(out, 51)
    # print(out)
