def count(n,text):
    """Function counts how many times the given letter appears in the given text"""
    ile = 0
    for i in text:
        if i == n:
            ile+=1
    return ile
print(count('e',"You never get a second chance to make a first impression"))
