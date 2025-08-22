from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):  # Class name should be capitalized by convention
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"

@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo_item = Todo(title=title, desc=desc)
        db.session.add(todo_item)
        db.session.commit()
    allTodo=Todo.query.all()
    return render_template("index.html", allTodo=allTodo)

@app.route("/show")
def products():
    allTodo=Todo.query.all()
    print(allTodo)
    return "This is the products page"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
