from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    surname = db.Column(db.String())
    date = db.Column(db.String())
    summ = db.Column(db.Integer)

    def __repr__(self):
        return f"Employee ({self.name}, {self.surname}, {self.date}, {self.summ})"
    

@app.route('/')
def index():
    sort_by = request.args.get('sort_by', None, type=str)
    sort_dir = request.args.get('sort_dir', None, type=str)
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    person = request.args.get('person', None, type=str)
    print("PERSON ", person)
    if person:
        try:
            results = Employee.query.filter_by(surname=person)\
                      .paginate(page=page, per_page=per_page)
        except:
            print("Something goes wrong")
    elif not sort_by:
        results = Employee.query.paginate(page=page, per_page=per_page)
    
    elif sort_by == 'name':
        if sort_dir == "desc":
            results = Employee.query.order_by(Employee.name.desc())\
                        .paginate(page=page, per_page=per_page)
        else:
            results = Employee.query.order_by(Employee.name.asc())\
                        .paginate(page=page, per_page=per_page)
    elif sort_by == 'surname':
        if sort_dir == "desc":
            results = Employee.query.order_by(Employee.surname.desc())\
                        .paginate(page=page, per_page=per_page)
        else:
            results = Employee.query.order_by(Employee.surname.asc())\
                        .paginate(page=page, per_page=per_page)
    elif sort_by == 'date':
        if sort_dir == "desc":
            results = Employee.query.order_by(Employee.date.desc())\
                        .paginate(page=page, per_page=per_page)
        else:
            results = Employee.query.order_by(Employee.date.asc())\
                        .paginate(page=page, per_page=per_page)
    elif sort_by == 'summ':
        if sort_dir == "desc":
            results = Employee.query.order_by(Employee.summ.desc())\
                        .paginate(page=page, per_page=per_page)
        else:
            results = Employee.query.order_by(Employee.summ.asc())\
                        .paginate(page=page, per_page=per_page)
    else:
        results = Employee.query.paginate(page=page, per_page=per_page)

    return render_template('index.html', results=results)


if __name__ == "__main__":
    app.run(debug=False)