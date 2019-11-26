from Maze import *
import math
import random


# 人
class Actor:
    # 場所
    position = None
    maze_connector = None
    name = None

    # 初期化
    def __init__(self, maze_connector, name, key):
        self.maze_connector = maze_connector
        self.position = self.generateInitialPosition()
        self.maze_connector.setActor(name, key, self.position)
        self.name = name

    # 初期位置生成
    def generateInitialPosition(self):
        while True:
            p = random.randrange(
                int(len(self.maze_connector.getInfoMaze()[0])))
            if self.moveTo(p):
                break
        return p

    # 移動する
    def moveTo(self, position):
        # 移動可能か
        if self.maze_connector.isCanMove(position):
            self.position = position
            self.maze_connector.setActorPosition(self.name, position)
            return True
        return False

    # 名前を返す
    def getName(self):
        return self.name

    # 現在地を返す
    def getPosition(self):
        return self.position


# 逃げるやつ
class Target(Actor):
    # 逃げるやつを設定
    def __init__(self, maze_connector, name):
        super().__init__(maze_connector, name, 1)

    # 逃げるやつの行動
    def main(self):
        while True:
            p = random.randrange(5) + 5
            position = self.maze_connector.moveRelative(self.name, p)
            if position is not 0:
                if self.moveTo(position):
                    return position


# 追跡者
class Chaser(Actor):
    # 報酬
    reward = Reward()

    # 見つけたflag
    flag = False

    # 追跡者を設定
    def __init__(self, maze_connector, name):
        super().__init__(maze_connector, name, 2)

    # フラグをセット
    def setFlag(self, flag):
        self.flag = flag

    # フラグをゲット
    def getFlag(self):
        return self.flag

    # 探索
    def searchTarget(self):
        # ゲーム終了してるか
        if self.maze_connector.isEnd():
            self.reward.giveReward('end')

        # 毎ターン
        self.reward.giveReward('turn')
        search_result = self.maze_connector.searchTarget(self.position)
        if not search_result:
            # 見つからなかった時
            target_p = None
            direction = None
            if self.getFlag():
                # フラグをセット
                self.setFlag(False)
            # 見失った報酬
            self.reward.giveReward('lost')
        else:
            # ターゲットの位置
            target_p = search_result[0]
            # ターゲットの方向
            direction = search_result[1]
            if not self.getFlag():
                # フラグセット
                self.setFlag(True)
            # 見つけた報酬
            self.reward.giveReward('find')

        return target_p, direction

    # メイン
    def main(self):

        p = self.searchTarget()
        if p[0] is not None:
            position = self.maze_connector.moveRelative(self.name, p)
            if position is not 0:
                if self.moveTo(position):
                    return
        else:
            while True:
                p = random.randrange(5) + 5
                position = self.maze_connector.moveRelative(self.name, p)
                if position is not 0:
                    if self.moveTo(position):
                        return


# if __name__ == "__main__":
#     data = [
#         0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
#         0, 1, 1, 0, 0, 0, 1, 0, 0, 0,
#         0, 1, 1, 0, 1, 0, 1, 0, 0, 0,
#         0, 0, 0, 0, 1, 0, 0, 0, 1, 0,
#         0, 0, 0, 0, 1, 0, 0, 0, 1, 0,
#         0, 1, 1, 0, 1, 0, 1, 1, 0, 0,
#         0, 0, 0, 0, 1, 0, 0, 1, 0, 1,
#         0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
#         0, 0, 0, 0, 1, 0, 0, 1, 0, 1,
#         0, 0, 0, 0, 1, 0, 0, 0, 0, 1
#     ]

#     maze = Maze(data, int(math.sqrt(len(data))))

#     # print(maze.isCanMove(-2, -2))
#     chre = Chaser(maze, 'chaser')
#     user = Target(maze, 'target')
#     while True:
#         if not maze.isEnd():
#             print(maze.actor_position)
#             p = chre.searchTarget()
#             print(p)
#             user.main()
#             chre.main()

#             print("報酬", chre.reward.getReward())
#             # input("")
#         else:
#             break

    # user
    # print(user.position)
    # print(chre.position)
