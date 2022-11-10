from app import db

#TABELA ŁACZACA M:N (wiele do wielu)
CONNECTED = db.Table('CONNECTED',
    db.Column('authorID', db.Integer, db.ForeignKey('author.id'), primary_key=True),
    db.Column('bookID', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)

#TABELA AUTOROW
class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), index=True)
   gender = db.Column(db.Text, index=True)
   nationality = db.Column(db.Text, index=True)
   CONNECTED = db.relationship('Book', secondary=CONNECTED, lazy='subquery', backref=db.backref('Author', lazy=True))

   def __str__(self):
       return f"<Author {self.name} ...>"

#TABELA KSIAZKI
class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.Text, index=True)
   genre = db.Column(db.Text, index=True)
   pages = db.Column(db.Integer, index=True)
   language = db.Column(db.Text, index=True)
   borrow_id = db.Column(db.Integer, db.ForeignKey('borrowed.id'))
   CONNECTED = db.relationship('Author', secondary=CONNECTED, lazy='subquery', backref=db.backref('Book', lazy=True))

   def __str__(self):
       return f"<Book {self.title}...>"

#TABELA WYPOŻYCZENIE
class Borrowed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Text, index=True)
    books = db.relationship("Book", backref="book", lazy="dynamic")
    
    def __str__(self):
       return f"<Borrow {self.status} ...>"
