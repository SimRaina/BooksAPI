from flask import Flask, jsonify, request, Response

app = Flask(__name__)

books = [
    {
            'name': 'Test Book 1',
            'price': 299,
            'isbn': 100,
            'author': 'Test Name 1'
        },
    {
            'name': 'Test Book 2',
            'price': 399,
            'isbn': 101,
            'author': 'Test Name 2'
         }
    ]

#GET /books
@app.route('/books')
def get_books():
    return jsonify({'books' : books})

def validBookObject(bookObject):
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject and "author" in bookObject):
        return True
    else:
        return False


@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if(validBookObject(request_data)):
        books.insert(0, request_data)
        return jsonify(request_data)
    else:
        return "False"

@app.route('/books/<int:isbn>')
def get_book_by_isbsn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
               'name': book["name"],
               'price': book["price"],
               'author': book["author"]
            }
    return jsonify(return_value)


@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    new_book = {
        'name': request_data['name'],
        'price': request_data['price'],
        'author': request_data['author'],
        'isbn': isbn
    }
    i=0;
    for book in books:
        currentIsbn = book["isbn"]
        if currentIsbn == isbn:
            books[i] = new_book
        i +=1
    return request_data

@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    i=0;
    for book in books:
        if book["isbn"] == isbn:
            books.pop(i)
        i +=1

    return "";

app.run(port = 5000)
