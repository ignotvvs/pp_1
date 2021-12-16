class Ebook():

    def __init__(self,title,author,pages):
        self.author = author
        self.title = title
        self.pages = pages
        self.current = 1
        self.is_opened = False


    def open_book(self):
        self.is_opened = True

    def close_book(self):
        self.is_opened = False

    def next_page(self):
        if self.current < self.pages and self.is_opened:
            self.current += 1
        else:
            print("Book is closed")

    def read_book(self,n):
        if self.is_opened and self.current < self.pages:
            self.current += n
        else:
            print("Book is closed")

    def previous_page(self):
        if self.current > 1 and self.is_opened:
            self.current -= 1
        else:
            print("Book is closed")

    def show_status(self):
        print(
f"""Title: {self.title}
Author: {self.author}
Pages: {self.pages}
Current page: {self.current}
""")


