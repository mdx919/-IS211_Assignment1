class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print('{title}, written by {author}.'.format(title=self.title, author=self.author))


b1 = Book('John Steinbeck', 'Of Mice and Men')
b2 = Book('Harper Lee', 'To Kill a Mockingbird')

b1.display()
b2.display()
