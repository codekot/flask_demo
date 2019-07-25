from app import db, Employee
from faker import Faker
import random

categories = ["first", "second", "third"]

if __name__ == '__main__':
    fake = Faker('ru_RU')
    db.create_all()
    for e in range(50):
        f_name = fake.name().split()
        f_date = fake.date()
        f_summ = random.randint(1000, 50000)
        emp = Employee(name=f_name[1], surname=f_name[0], 
                       date=f_date, summ=f_summ)
        db.session.add(emp)
    db.session.commit()
    print("Database populated")
