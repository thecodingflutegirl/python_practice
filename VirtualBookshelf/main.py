from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# import sqlite3

# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute(
#     "INSERT INTO books VALUES(3, 'Good Earth', 'Pearl s. Buck', '9.3')")
# db.commit()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-read.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(240), unique=True, nullable=False)
    author = db.Column(db.String(240), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()

# JUST AS AN EXAMPLE OF HARD CODING IT
# new_book = Books(id=1, title="Harry Potter", author="JK Rowling", rating=9.3)
# db.session.add(new_book) #creates new data
# db.session.commit()


@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        new_book = Books(
            title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        book_id = request.form['id']
        update_book = Books.query.get(book_id)
        update_book.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Books.query.get(book_id)
    return render_template('edit.html', book=book_selected)


@app.route('/delete', methods=["POST", "GET"])
def delete():
    book_id = request.args.get('id')
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
