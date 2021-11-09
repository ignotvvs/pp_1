def sum(array):
    x = 0
    for i in array:
        x+=i
    return x
def array2str(array):
    x = ""
    for i in array:
        x += f"{i} "
    return x
#print(f"Sum of values: {sum([4,3,7,1,3])}\nArray: {array2str([4,3,7,1,3])}")
