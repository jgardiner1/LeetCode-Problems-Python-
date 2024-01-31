import random


class RandomizedSet:
    def __init__(self):
        self.d = dict()
        self.a = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False

        self.d[val] = len(self.d)
        self.a.append(val)

        self.printInfo()
        return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            if len(self.a) <= 1:
                self.d.pop(val)
                self.a.pop()
                self.printInfo()
                return True

            removedIndex = self.d[val]
            self.d.pop(val)

            if removedIndex == len(self.a) - 1:
                self.a.pop()
                self.printInfo()
                return True

            lastItem = self.a.pop()

            self.a[removedIndex] = lastItem
            self.d[lastItem] = removedIndex

            self.printInfo()
            return True

        self.printInfo()

        return False

    def getRandom(self) -> int:
        if len(self.a) == 1:
            return self.a[0]

        return self.a[random.randint(0, len(self.a) - 1)]

    def printInfo(self):
        print(self.d, " ", self.a)


[
    "insert",
    "insert",
    "getRandom",
    "getRandom",
    "insert",
    "remove",
    "getRandom",
    "getRandom",
    "insert",
    "remove",
]
[[3], [3], [], [], [1], [3], [], [], [0], [0]]
obj = RandomizedSet()
print("inserting 3")
print(obj.insert(3), "\n")
print("inserting 3")
print(obj.insert(3), "\n")
print(obj.getRandom())
print(obj.getRandom())
print("inserting 1")
print(obj.insert(1), "\n")
print("removing 3")
print(obj.remove(3), "\n")
print(obj.getRandom())
print(obj.getRandom())
print("inserting 0")
print(obj.insert(0), "\n")
print("removing 0")
print(obj.remove(0), "\n")
