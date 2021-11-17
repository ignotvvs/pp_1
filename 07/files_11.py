film_titles = ["Pulp fiction","Interstellar","Joker","Home alone","Inception"]
with open("movies.txt","w") as file:
    for i in film_titles:
        file.write(i + "\n")