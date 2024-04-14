from flask import Flask, request

app = Flask(__name__)

# Create routes

@app.route('/book/<int:book_id>')
def read_book_by_id(book_id):
    return f"book id is: {book_id}"


@app.route('/book', methods=['POST'])
def create_book():
    book_name = request.json.get('book_name')
    author = request.json.get('author')
    publisher = request.json.get('publisher')
    return f"book name: {book_name}, author: {author}, publisher: {publisher}"