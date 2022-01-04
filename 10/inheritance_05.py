class Music:
    def __init__(self,artist,trackTitle,album,year):
        self.artist = artist
        self.trackTitle = trackTitle
        self.album = album
        self.year = year

    def __str__(self):
        return f"""Performer:   {self.artist}
Song:        {self.trackTitle}
Album:       {self.album}
Year:        {self.year}
"""


music1 = Music('Edd Sheeran',"Hearts Don't Break Around Here",'Divide',"2017")
print(music1)
music2 = Music('Home','Resonance',"Odyssey",'2014')
print(music2)
music3 = Music('Tame Impala', 'One More Year',"The Slow Rush",'2020')
print(music3)