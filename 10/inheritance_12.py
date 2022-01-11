from random import randint
class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

    @staticmethod
    def print_in_row(array):
        for i in array:
            if array.index(i) == len(array)-1: print(i)
            else: print(f"{i}, ",end='')

    @staticmethod
    def create_same(n,v):
        #a = n*[v]
        a = []
        for i in range(n):
            a.append(v)
        return a

    @staticmethod
    def create_random(n,f,to):
        a = []
        for i in range(n):
          x = randint(f,to)
          a.append(x)
        return a

    @staticmethod
    def determine(a,f,t):
        count = 0
        for i in a:
            if f <= i <= t: count+=1
        return count


my_array = [4, 1, 8, 7, 2]
Arrays.print_in_col(my_array)
Arrays.print_in_row(my_array)
tab1 = Arrays.create_same(10,4)
print(tab1)
tab2 = Arrays.create_random(20,-7,8)
print(tab2)
print(Arrays.determine(tab2,-1,1))
