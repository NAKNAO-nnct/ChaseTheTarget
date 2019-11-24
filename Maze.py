# -*- coding: utf-8 -*-
import random
import math


# 報酬管理
class Reward:
    reward = None

    # 初期化
    def __init__(self):
        self.reward = 0

    # 報酬を与える
    # def


# 迷路クラス
class Maze:
    maze_data = []
    maze_x = 0
    # maze_y = 0

    actor_position = [
        ['参加者名', '1: 逃げる, 2:　追う', '座標']
    ]

    # 初期化
    def __init__(self, maze_data, maze_len):
        self.maze_data = maze_data
        self.maze_x = maze_len
        # self.maze_y = maze_y
        self.actor_position = []

    # 迷路情報を取得
    def getInfoMaze(self):
        return [self.maze_data, self.maze_x]

    # 参加者を取得
    def getActor(self):
        return self.actor_position

    # 参加者セット
    def setActor(self, name, key, position):
        self.actor_position.append([name, key, position])

    # 移動可能か
    def isCanMove(self, p):
        try:
            if p < 1:
                return False
            if (self.maze_data[p - 1] == 0):
                return True
        except:
            return False
        return False

    # 追跡者の探索範囲にtargetがいるか
    # いれば座標をいなければnoneを返す
    def searchTarget(self, position):
        # 列数
        column = self.getInfoMaze()[1]

        # 追跡者の点p
        p = position

        # 追跡者のいる行
        act_row = int(math.ceil(p / column))

        '''
        方向
        5: 左
        6: 右
        7: 下
        8: 上
        '''

        # 横方向(マイナス)
        # 移動可能マス
        available_square = []
        for i in range(p - 1, column * (act_row - 1), -1):
            # 移動可能か
            if self.isCanMove(i):
                available_square.append(i)
            else:
                break
        # 探索範囲にいるか
        for i in available_square:
            if self.actor_position[1][2] == i:
                return i, 5

        # 横方向(プラス)
        # 移動可能マス
        available_square = []
        for i in range(p + 1, column * act_row):
            # 移動可能か
            if self.isCanMove(i):
                available_square.append(i)
            else:
                break
        # 探索範囲にいるか
        for i in available_square:
            if self.actor_position[1][2] == i:
                return i, 6

        # 縦方向(マイナス)
        # 移動可能マス
        available_square = []
        for i in range(-1, -column, -1):
            # 移動可能か
            if self.isCanMove(p - column * i):
                available_square.append(p - column * i)
            else:
                break
        # 探索範囲にいるか
        for i in available_square:
            if self.actor_position[1][2] == i:
                return i, 7

        # 縦方向(プラス)
        # 移動可能マス
        available_square = []
        for i in range(1, column):
            # 移動可能か
            if self.isCanMove(p + column * i):
                available_square.append(p + column * i)
            else:
                break
        # 探索範囲にいるか
        for i in available_square:
            if self.actor_position[1][2] == i:
                return i, 8

        return False


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
            if self.maze_connector.isCanMove(p):
                break
        return p

    # 移動する
    def moveTo(self, position):
        # 移動可能か
        if self.maze_connector.isCanMove(position):
            self.position = position
            return True
        return False


# 逃げるやつ
class Target(Actor):
    # 逃げるやつを設定
    def __init__(self, maze_connector, name):
        super().__init__(maze_connector, name, 1)


# 追跡者
class Chaser(Actor):
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
        search_result = self.maze_connector.searchTarget(self.position)
        if not search_result:
            # 見つからなかった時
            target_p = None
            direction = 100
            pass
        else:
            # ターゲットの位置
            target_p = search_result[0]
            # ターゲットの方向
            direction = search_result[1]

        return target_p, direction


if __name__ == "__main__":
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
    maze = Maze(data, int(math.sqrt(len(data))))

    # print(maze.isCanMove(-2, -2))
    chre = Chaser(maze, 'chaser')
    user = Target(maze, 'target')

    print(maze.actor_position)
    print(chre.searchTarget())

    # user
    # print(user.position)
    # print(chre.position)
