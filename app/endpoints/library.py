from flask import Blueprint, jsonify, request
from app import db
from sqlalchemy import desc

from app.models.library import Book, Litterateur, Rating
books_blueprint = Blueprint('books', __name__)
litterateurs_blueprint = Blueprint('litterateurs', __name__)


########################################################################
@books_blueprint.route('/books', methods=['GET'])
@books_blueprint.route('/books/<int:page>', methods=['GET'])
def get_books(page = 1):
    return jsonify({
        'results': [b.serialized_for_books for b in Book.query.paginate(page, 3, False).items]
    })

@books_blueprint.route('/book/<id>', methods=['GET'])
def get_book(id):
    return jsonify({
        'results': Book.query.get(id).serialized
    })

@books_blueprint.route("/book", methods=["POST"])
def create_book():
    dict_body = request.get_json()
    book_data = Book(**dict_body)

    db.session.add(book_data)
    db.session.flush()

    rate_data = Rating(book_id=book_data.id)

    db.session.add(rate_data)
    db.session.commit()

    return jsonify(book_data.serialized)

@books_blueprint.route("/book/<id>", methods=['PUT'])
def update_product_detail(id):
    book_for_up = Book.query.get(id)
    name = request.json['name']
    book_for_up.name = name

    db.session.commit()

    return jsonify(book_for_up.serialized)

@books_blueprint.route("/book/<id>", methods=["DELETE"])
def delete_book(id):
    book_delete = Book.query.get(id)
    db.session.delete(book_delete)
    db.session.commit()
    data = {"results": "Successful removal"}

    return jsonify(data)
##########################################################################
@litterateurs_blueprint.route('/litterateurs', methods=['GET'])
@litterateurs_blueprint.route('/litterateurs/<int:page>', methods=['GET'])
def get_litterateurs(page = 1):
    return jsonify({
        'results': [l.serialized_for_litterateurs for l in Litterateur.query.paginate(page, 3, False).items]
    })

@litterateurs_blueprint.route('/litterateur/<id>', methods=['GET'])
def get_litterateur(id):
    return jsonify({
        'results': Litterateur.query.get(id).serialized
    })


@litterateurs_blueprint.route("/litterateur", methods=["POST"])
def create_litterateur():
    dict_body = request.get_json()
    litterateur_data = Litterateur(**dict_body)

    db.session.add(litterateur_data)
    db.session.commit()

    return jsonify(litterateur_data.serialized)


@litterateurs_blueprint.route("/litterateur/<id>", methods=['PUT'])
def update_litterateur_detail(id):
    litterateur_for_up = Litterateur.query.get(id)
    name = request.json['name']
    surname = request.json['surname']

    litterateur_for_up.name = name
    litterateur_for_up.surname = surname
    db.session.commit()

    return jsonify(litterateur_for_up.serialized)

@litterateurs_blueprint.route("/litterateur/<id>", methods=["DELETE"])
def delete_litterateur(id):
    litterateur_delete = Litterateur.query.get(id)
    db.session.delete(litterateur_delete)
    db.session.commit()
    data = {"results": "Successful removal"}

    return jsonify(data)
#############################################################################
@books_blueprint.route('/rating/<id>', methods=['GET'])
def get_rating(id):
    return jsonify({
        'results': Rating.query.get(id).serialized
    })

@books_blueprint.route("/rating/<id>", methods=['PUT'])
def update_raiting_book(id):
    rating_for_up = Rating.query.get(id)

    sum = request.json['rate']
    act = request.json['act']

    if 0 < int(sum) <= 5 and act == 'plus':
        rating_for_up.sum = int(rating_for_up.sum) + int(sum)
        rating_for_up.qu = rating_for_up.qu + 1
        rating_for_up.rating = round(rating_for_up.sum / rating_for_up.qu)
        db.session.commit()
        return jsonify(rating_for_up.serialized)
    elif 0 < int(sum) <= 5 and act == 'minus' and int(rating_for_up.sum) > int(sum):
        rating_for_up.sum = int(rating_for_up.sum) - int(sum)
        rating_for_up.qu = rating_for_up.qu - 1
        rating_for_up.rating = round(rating_for_up.sum / rating_for_up.qu)
        db.session.commit()
        return jsonify(rating_for_up.serialized)
    else:
        data = {"results": "Rating out of range 0-5"}
        return jsonify(data)
