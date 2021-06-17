import random

class countdownNumbers:
    def __init__(self, nbr_numbers=6, min_target=100, max_target=999):
        self.nbr_small = nbr_numbers
        self.min = min_target
        self.max = max_target

        self.nbr_big = 0
        self.target = 0
        self.numList = []

    def start(self):
        self.getBigNbrs()
        self.getNbrs()
        self.genTarget()
        self.printAll()

    def getBigNbrs(self):
        self.nbr_big = int(input("How many big numbers would you like (0-4): "))
        if self.nbr_big > 4:
            self.nbr_big = 4
        elif self.nbr_big < 0:
            self.nbr_big = 0

        self.nbr_small = self.nbr_small - self.nbr_big

    def getNbrs(self):
        bigNbrs = [100,75,50,25]
        smallMax = 10

        for i in range(self.nbr_big):
            self.numList.append(bigNbrs[random.randint(0,len(bigNbrs)-1)])
        
        for i in range(self.nbr_small):
            self.numList.append(random.randint(1,smallMax))

        self.numList.sort(reverse=True)

    def genTarget(self):
        self.target = random.randint(self.min,self.max)

    def printAll(self):
        print(f"nbr_small: {self.nbr_small}")
        print(f"nbr_big: {self.nbr_big}")
        print(f"min: {self.min}")
        print(f"max: {self.max}")
        print(f"target: {self.target}")
        print(f"numList: {self.numList}")

    def solve(self):
        print("Pls help")

cN = countdownNumbers()
cN.start()