import random


# 迷路クラス
class Maze:

    maze_data = []
    maze_x = 0
    maze_y = 0

    actor_position = [
        ['参加者名', '0: 逃げる, 1:　追う', ['x座標', 'y座標']]
    ]

    # 初期化
    # 迷路データを渡す
    def __init__(self, maze_data):
        self.maze_data = maze_data
        self.maze_x = len(maze_data)
        self.maze_y = len(maze_data[0])
        self.actor_position = []

    # 参加者セット
    def setActor(self, name, key, position):
        self.actor_position.append([name, key, position])

    # 移動可能か
    def isCanMove(self, x, y):
        try:
            if x < 0 or y < 0:
                return False
            if(self.maze_data[y][x] == 0):
                return True
        except:
            return False
        return False

    # Actorを(0,0)とした時の迷路座標との変換
    def getConvertPosition(self, act_position):
        abs_position = []
        for i in range(1 - int(self.maze_x/2) + 1, int(self.maze_x/2) + 1):
            for j in range(1 - int(self.maze_y / 2) + 1, int(self.maze_y / 2) + 1):
                # if i == 0 and j == 0:
                #     abs_position.append([None, None])
                if self.isCanMove(act_position[0] + j, act_position[1] + i):
                    abs_position.append(
                        [act_position[0] + j, act_position[1] + i]
                    )
                else:
                    abs_position.append([None, None])
        return abs_position

    # 追跡者の探索範囲に逃げてるやつがいるか
    # いれば座標をいなければnoneを返却
    def searchTarget(self):
        count = 0
        relative_chaser = self.getConvertPosition(
            self.actor_position[0][2])
        absolute_chaser = self.actor_position[0][2]

        relative_maze_num = relative_chaser.index(absolute_chaser)
        maze_x_half = self.maze_x % relative_maze_num

        for i in range():
            pass

        return maze_x_half
        # return count


# 人
class Actor():
    # 場所
    position = []
    maze_connector = None
    name = None

    #
    def __init__(self, maze_connector, name, key):
        self.maze_connector = maze_connector
        initial_position = self.generateInitialPosition()
        self.position = [initial_position[0], initial_position[1]]
        self.maze_connector.setActor(name, key, self.position)
        self.name = name

    # 初期位置生成
    def generateInitialPosition(self):
        while (True):
            _x = random.randrange(self.maze_connector.maze_x)
            _y = random.randrange(self.maze_connector.maze_x)
            if self.maze_connector.isCanMove(_x, _y):
                break
        return (_x, _y)

    # 移動する
    def moveTo(self, position):
        # 移動できるか
        if self.maze_connector.isCanMove(position[0], position[1]):
            self.position = position


# 逃げる人
class Target(Actor):
    def __init__(self, maze_connector, name):
        super().__init__(maze_connector, name, 0)


# 追跡者
class Chaser(Actor):
    # 見つけたflag
    flag = False

    def __init__(self, maze_connector, name):
        super().__init__(maze_connector, name, 1)

    # フラグ管理
    def setFlag(self, flag):
        self.flag = flag

    # 探索
    def searchTarget(self):
        seach_range = self.maze_connector.getConvertPosition(self.name)
        pass

    # 探索可能範囲の取得
    def getSearchRange(self):
        _local_x = self.position[0]
        _local_y = self.position[1]
        maze_data = self.maze_connector

        pass


if __name__ == "__main__":
    data = [
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    ]
    maze = Maze(data)

    # print(maze.isCanMove(-2, -2))
    chre = Chaser(maze, 'chaser')
    user = Target(maze, 'target')

    print(maze.actor_position)
    print(maze.searchTarget())

    # user
    # print(user.position)
    # print(chre.position)
