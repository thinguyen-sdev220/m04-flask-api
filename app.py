from flask import Flask

app = Flask(__name__)

# Create routes

@app.route('/book/<int:book_id>')
def read_book_by_id(book_id):
    return f"book id is: {book_id}"