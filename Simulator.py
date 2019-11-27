# import math
# from Maze import *


# # シミュレータ
# class Simulator:
#     maze = None

#     def __init__(self, maze_conncet, position):
#         # self.maze = maze_conncet
#         self.maze = Maze(maze_conncet, 10)
#         self.maze.setActors([])

#     # 状態を取得
#     def getState(self):
#         pass

#     # 引数actionを実行する
#     def doAction(self, action):

#         pass

#     pass


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
#     s = len(maze.getInfoMaze()[0])
#     q = [[], [], [], []]
#     print(q[0])
