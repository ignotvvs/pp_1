
import json

movie = {
    "name": "Loving Vincent",
    "year": 2017,
    "directors": ["Dorota Kobiela", "Hugh Welchman"],
    "awarded": True,
    "genre": "Animation/Drama"
}

with open("favourite.json","w") as file:
    json.dump(movie,file,indent = 4)

