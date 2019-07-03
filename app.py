from flask import Flask, jsonify
from flask import request, Response
import json
from settings import *

#app = Flask(__name__)
#app.config['DEBUG'] = True

books = [
    {
        'name':'How to Win Friends & Influence People',
        'price': 200,
        'isbn': 8945131232
    },
    {
        'name': 'Think and Grow Rich',
        'price': 542,
        'isbn': 4646513684
    },
    {
        'name': 'Man’s Search for Meaning',
        'price': 789,
        'isbn': 944557422
    },
    {
        'name': 'Awaken the Giant Within',
        'price': 235,
        'isbn': 5684651636
    },
    {
        'name': 'As A Man Thinketh',
        'price': 456,
        'isbn': 4545465465
    },
    {
        'name': 'The Power of Positive Thinking',
        'price': 900,
        'isbn': 65446456565
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
        response.headers['Location']= "/books/" + str(new_books['isbn'])
        return response
    else:
        invalifBookObkectErroMsg = {
            "error": "Invlaid book object passed in request",
            "helpstring": "Data passed in similar to this{'name': 'bookname', 'price': 450, 'isbn': 89465465}"
        }
        response = Response(json.dumps(invalifBookObkectErroMsg), status=400, mimetype='applicatio/json');
        return response


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
# PUT /boooks/8945131232
#{
#   'name' = 'Raghu',
#   'price' = 14
#}
@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data= request.get_json()
    new_book = {
        'name' : request_data['name'],
        'price': request_data['price'],
        'isbn': isbn
    }
    i =0;
    for book in books:
        cureentIsbn = book["isbn"]
        if cureentIsbn == isbn:
            books[i] = new_book
        i += 1
    response = Response("", status=204)
    return response
#PATCH /books/4566231

@app.route('/books/<int:isbn>', methods=['PATCH'])
def update_book(isbn):
    request_data= request.get_json()
    update_book = {}
    if("name" in request_data):
        update_book["name"] = request_data['name']
    if ("price" in request_data):
        update_book["price"] = request_data['price']
    for book in books:
        if book["isbn"]== isbn:
            book.update(update_book)
    response = Response("", status=204)
    response.headers['Location'] = "/books/" + str(isbn)
    return response

# DELETE /books/4545465465

@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    i =0;
    for book in books:
        if book["isbn"]== isbn:
            #return jsonify(book)
            books.pop(i)
        i += 1


    return "";

app.run(port=5000)