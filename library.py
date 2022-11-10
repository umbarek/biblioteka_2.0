from app import app, db
from app.models import Author, Book, Borrowed

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "User": Author,
       "Post": Book,
       "Borrowed": Borrowed
   }