from app import db

#TABELA ŁACZACA M:N (wiele do wielu)
AuthorBook = db.Table('AuthorBook',
    db.Column('authorID', db.Integer, db.ForeignKey('author.id'), primary_key=True),
    db.Column('bookID', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)

#TABELA AUTOROW
class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), index=True)
#   bookID = db.Column(db.Integer, db.ForeignKey('book.id'))


#   books = db.relationship('Book', secondary=books, lazy='subquery',
#        backref=db.backref('Author', lazy=True))

   def __str__(self):
       return f"<Author {self.surname} ...>"


#TABELA KSIAZKI
class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.Text, index=True)
   author = db.relationship("Author", backref="book", lazy="dynamic")
   genre = db.Column(db.Text, index=True)
   pages = db.Column(db.Integer, index=True)
   cover = db.Column(db.Text, index=True)
   language = db.Column(db.Text, index=True)
   borrow = db.relationship("Borrow", backref="borrowed", lazy="dynamic")
#   authorID = db.Column(db.Integer, db.ForeignKey('author.id'))
   

   def __str__(self):
       return f"<Book {self.title}...>"


#TABELA WYPOŻYCZENIE
class Borrow(db.Model):
   status = db.Column(db.Text, primary_key=True)
   bookID = db.Column(db.Integer, db.ForeignKey('book.id'))

   book = db.relationship("Book", backref="borrowed", lazy="dynamic")
   
   def __str__(self):
       return f"<Borrow {self.status} ...>"

