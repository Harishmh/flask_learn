from flask import Flask, jsonify
app = Flask(__name__)

books = [
    {
        'name':'book1',
        'price': 200,
        'isbn': 8945131232
    },
    {
        'name': 'book2',
        'price': 900,
        'isbn': 96857422
    }
]
# GET /books
@app.route('/books')
def get_books():
    return jsonify({'books': books})

# GET /books/96857422
@app.route('/books/<int:isbn>')
def get_books_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }

    return jsonify(return_value)


app.run(port=5000)