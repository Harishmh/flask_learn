from flask import Flask, jsonify
from flask import request, Response
app = Flask(__name__)
app.config['DEBUG'] = True

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
# POST
def validBookObject(bookObject):
    if ("name" in bookObject and "price" in  bookObject and "isbn" in bookObject):
        return True
    else:
        return False

@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()

    if(validBookObject(request_data)):
        new_books = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": request_data['isbn']
        }
        books.insert(0, new_books)
        response= Response("", 201, mimetype='application/json')
        return response
    else:
        return "False"


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