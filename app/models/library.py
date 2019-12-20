from app import db

##################################################################
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False)
    rating = db.relationship('Rating', back_populates="book", cascade="all, delete, delete-orphan", lazy='select')
    litterateurs = db.relationship('Litterateur', secondary='books_litterateurs', backref='books')

    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'rating': [r.serialized_for_book for r in self.rating],
            'litterateurs': [l.serialized_for_litterateurs for l in self.litterateurs]
        }

    @property
    def serialized_for_books(self):
        return {
            'id': self.id,
            'name': self.name,
            'rating': [r.serialized_for_book for r in self.rating]
        }



class Litterateur(db.Model):
    __tablename__ = 'litterateurs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(50), nullable=False)
    surname = db.Column(db.Unicode(50), nullable=False)

    books_litterateur = db.relationship('Book', secondary='books_litterateurs', backref='litterateursa')

    @property
    def serialized_for_litterateurs(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname
        }

    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'books': [b.serialized_for_books for b in self.books_litterateur],
        }

books_litterateurs = db.Table('books_litterateurs',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('litterateur_id', db.Integer, db.ForeignKey('litterateurs.id'), primary_key=True)
)

class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    sum = db.Column(db.Integer, default=0)
    qu = db.Column(db.Integer, default=0)
    rating = db.Column(db.Integer, default=0)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    book = db.relationship("Book", back_populates="rating")

    @property
    def serialized_for_book(self):
        return {
            # 'id': self.id,
            # 'sum': self.sum,
            # 'qu': self.qu,
            'rating': self.rating
        }

    @property
    def serialized(self):
        return {
            'id': self.id,
            'sum': self.sum,
            'qu': self.qu,
            'rating': self.rating
        }
