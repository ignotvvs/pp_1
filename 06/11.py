import I0
def compare(array1,array2):
    if array1 == array2:
            return True
    return False
array1 = ["water","book","sky"]
array2 = ["water","boo0k","sky"]
print(f"Array1: {I0.array2str(array1)}")
print(f"Array2: {I0.array2str(array2)}")
print("Comparison: arrays are the same") if compare(array1,array2) == True else print("Comparison: not the same")