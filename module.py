import os
import time


class HanoiTower:
    TOWER = list()
    MAX = int()
    COUNT = int()

    TEXT_HEAD = str()
    TEXT_DATA = str()

    @classmethod
    def moveStone(cls, start: int, end: int) -> bool:
        cls.COUNT += 1
        if cls.moveCheck(start, end):
            data = cls.TOWER[start - 1].pop()
            cls.TOWER[end - 1].append(data)
            print(f"!! {cls.COUNT}' moved : [Tower{start}] -> [Tower{end}]")
            cls.display()
            return True
        else:
            print(f"!! {cls.COUNT}' move failed : [Tower{start}] -> [Tower{end}]")
            cls.display()
            return False

    @classmethod
    def moveCheck(cls, start: int, end: int) -> bool:
        startLen = len(cls.TOWER[start - 1])
        if startLen <= 0:
            return False
        data1 = cls.TOWER[start - 1][startLen - 1]

        endLen = len(cls.TOWER[end - 1])
        if endLen <= 0:
            return True
        else:
            data2 = cls.TOWER[end - 1][endLen - 1]
            if data1 >= data2:
                return False
            else:
                return True

    @classmethod
    def display(cls) -> None:
        TEXT_HEAD = list()
        TEXT_DATA = list()

        time.sleep(1)
        os.system("cls")
        print("                   ")
        print("|     |     |     |")
        for mI in range(cls.MAX):
            cls.TEXT_HEAD = ""
            cls.TEXT_DATA = ""
            for tI in range(len(cls.TOWER)):
                cls.makeData(tI, cls.MAX - mI)
            cls.TEXT_HEAD += "|"
            cls.TEXT_DATA += "|"

            print(cls.TEXT_HEAD)
            print(cls.TEXT_DATA)
        print("|_____|_____|_____|")
        print("                   ")

    @classmethod
    def makeData(cls, tCurr: int, mCurr: int) -> None:
        if len(cls.TOWER[tCurr]) >= mCurr:
            cls.TEXT_HEAD += f"|-----"
            cls.TEXT_DATA += f"|  {cls.TOWER[tCurr][mCurr - 1]}  "
        else:
            cls.TEXT_HEAD += f"|     "
            cls.TEXT_DATA += f"|     "

    @classmethod
    def setMax(cls, max: int) -> None:
        cls.MAX = max

        cls.TOWER.append(list())
        cls.TOWER.append(list())
        cls.TOWER.append(list())

        for mI in range(max):
            cls.TOWER[0].append(max - mI)

    @classmethod
    def solveHanoi(cls, N: int, start: int, end: int, mid: int) -> None:
        if N == 1:
            cls.moveStone(start, end)
        else:
            cls.solveHanoi(N - 1, start, mid, end)
            cls.moveStone(start, end)
            cls.solveHanoi(N - 1, mid, end, start)
