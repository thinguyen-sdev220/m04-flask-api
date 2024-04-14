from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return dict(id=self.id, book_name=self.book_name, author=self.author, publisher=self.publisher)


# Create routes

@app.route('/book/<int:book_id>')
def read_book_by_id(book_id):
    book = db.get_or_404(Book, book_id)
    return book.to_dict()


@app.route('/book', methods=['POST'])
def create_book():
    book_name = request.json.get('book_name')
    author = request.json.get('author')
    publisher = request.json.get('publisher')

    book = Book(book_name=book_name, author=author, publisher=publisher)
    db.session.add(book)
    db.session.commit()

    return book.to_dict()


@app.route('/book/<int:book_id>', methods=["PUT", "PATCH"])
def update_book(book_id):
    book = db.get_or_404(Book, book_id)
    book_name = request.json.get('book_name')
    author = request.json.get('author')
    publisher = request.json.get('publisher')

    if book_name is not None:
        book.book_name = book_name

    if author is not None:
        book.author = author

    if publisher is not None:
        book.publisher = publisher

    db.session.commit()

    return book.to_dict()


@app.route('/book/<int:book_id>', methods=["DELETE"])
def delete_book(book_id):
    return f"book id is: {book_id}"