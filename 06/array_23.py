from array_18 import bubblesort

def median(a):
    if len(a)%2 != 0:
        return a[len(a)//2]
    x = a[len(a)//2]
    b = a[len(a)//2-1]
    return (x+b)/2

tab1 = [1,0,9,4,6,9]
tab2 = [6,8,3,1,0,5,7]

print(f"Array: {tab1}\nMedian: {median(bubblesort(tab1))}")
print(f"Array: {tab2}\nMedian: {median(bubblesort(tab2))}")

