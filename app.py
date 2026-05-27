from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Library:
    def __init__(self, books):
        self.books = books

    def display(self):
        return self.books

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def return_book(self, book):
        self.books.append(book)


books=["C++","Java","Python"]

lb=Library(books)

@app.route("/")
def home():
    return render_template("index.html",books=lb.display())


@app.route("/borrow",methods=["POST"])
def borrow():

    book=request.form["book"]
    lb.borrow_book(book)

    return redirect("/")


@app.route("/returnbook",methods=["POST"])
def returnbook():

    book=request.form["book"]
    lb.return_book(book)

    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)