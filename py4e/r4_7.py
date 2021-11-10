def computegrade(score):
    if score>0.0 and score<1.0:
        if score >= 0.9: return "A"
        elif score >= 0.8: return "B"
        elif score >= 0.7: return "C"
        elif score >= 0.6: return "D"
        else: return "F"
    else: return "Invalid"
try:
    s = float(input("Enter your score: "))
    print(computegrade(s))
except: print("Invalid")