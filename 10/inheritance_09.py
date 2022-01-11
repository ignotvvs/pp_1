class Book:
    def __init__(self,title,author,genre):
        self.title = title
        self.author = author
        self.genre = genre
    def read_book(self):
        print("Reading book...")
    def __str__(self):
        return f"""Title:    {self.title}
Author:   {self.author}
Genre:    {self.genre}"""


class Ebook(Book):
    def __init__(self,file,title,author ,genre):
        self.file = file
        super().__init__(title,author,genre)
    def __str__(self):
        return f"""{super().__str__()}
File:     {self.file}
"""


class PaperBook(Book):
    def __init__(self,pages,title,author,genre):
        self.pages = pages
        super().__init__(title,author,genre)
    def __str__(self):
        return f"""{super().__str__()}
Pages:    {self.pages}
"""


book1 = PaperBook('145',"Harry Potter and The Prisoner of Azkaban","J.K. Rowling","fantasy")
book2 = Ebook("ebook.pdf",'1984','George Orwell',"fiction")
print(book2)
print(book1)

