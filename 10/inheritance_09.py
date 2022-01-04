class Book:
    def __init__(self,title,author,genre):
        self.title = title
        self.author = author
        self.genre = genre

    def read_book(self):
        print("Reading book...")

class Ebook(Book):
    def __init__(self,file,title,author ,genre):
        self.file = file
        super().__init__(title,author,genre)

