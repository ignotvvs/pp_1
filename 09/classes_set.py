class Statistics():
    def __init__(self):
        self.set = []


    def add_number(self):
        while True:
            x = input("Enter a number: ")
            if x == 'o':
                break
            x = int(x)
            if x not in self.set: self.set.append(x)

    def greatest(self):
        maks = self.set[0]
        for i in self.set:
            if i > maks:
                maks = i

        self.maks = maks
        return self.maks

    def smallest(self):
        minn = self.set[0]
        for i in self.set:
            if i < minn:
                minn = i

        self.minn = minn
        return self.minn

    def mean(self):
        total = 0
        for i in self.set:
            total += i
        self.avg = total / len(self.set)
        return self.avg

    def median(self):
        self.set.sort()
        if len(self.set) % 2:
            self.mediana = self.set[(len(self.set) // 2) ]
        else:
            self.mediana = self.set[(len(self.set) // 2)] + self.set[(len(self.set) // 2)//2-1]

        return self.mediana
    def display(self):
        for i in self.set:
            if self.set.index(i) == len(self.set)-1:
                print(i)
            else:
                print(i, end=", ")
        print(
f"""
Minimum: {self.smallest()}
Maximum: {self.greatest()}
Avg: {self.mean()}
Median: {self.median()}
""")

nums = Statistics()
nums.add_number()
nums.display()
print(nums.mediana)





