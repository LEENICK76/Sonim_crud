from flask import Flask, jsonify, request

app = Flask(__name__)

libraries = [
    {
        'name': 'FICTIONAL LIBRARY',
        'books': [
            {
                'name': 'Precious Stones',
                'price': 700
            }
        ]
    }
]


@app.route('/library', methods=['POST'])
def create_library():
    request_data = request.get_json()
    new_library = {
        'name': request_data['name'],
        'books': []
    }
    libraries.append(new_library)
    return jsonify(new_library)


@app.route('/library/<string:name>')
def get_library(name):
    for library in libraries:
        if library['name'] == name:
            return jsonify(library)
    return jsonify({'Message': 'Library not found'})


@app.route('/library')
def get_libraries():
    return jsonify({'libraries': libraries})


@app.route('/library/<string:name>/books', methods=['POST'])
def create_books_in_library(name):
    request_book_data = request.get_json()
    for library in libraries:
        if library['name'] == name:
            new_book = {
                'name': request_book_data['name'],
                'price': request_book_data['price']
            }
            return jsonify(new_book)

    return jsonify({'Message': 'Library not found'})


@app.route('/library/<string:name>/<string:book_name>')
def get_price_of_book_in_library(name, book_name):
    for library in libraries:
        if library['name'] == name:
            books = library['books']
            for book in books:
                if book['name'] == book_name:
                    return jsonify({'price': book['price']})
    return jsonify({'Message': 'Book not found'})


@app.route('/library/<string:name>/books')
def get_books_in_library(name):
    for library in libraries:
        if library['name'] == name:
            return jsonify({'books': library['books']})
    return jsonify({'Message': 'Book not found'})


if __name__ == '__main__':
    app.run(debug=True)
