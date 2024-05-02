import module as DS

hanoi = DS.HanoiTower

MAX = 7
hanoi.setMax(MAX)
hanoi.display()
hanoi.solveHanoi(MAX, 1, 3, 2)
hanoi.display()