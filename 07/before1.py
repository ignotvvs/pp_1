import re

txt = r"The rain in Spa\nainn"
x = re.search(r"\b(Spa)\\n.*",txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")