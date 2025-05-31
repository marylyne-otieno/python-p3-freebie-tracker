#!/usr/bin/env python
from models import Company, Dev, Freebie, session
def seed_data():

    session.query(Freebie).delete()
    session.query(Company).delete()
    session.query(Dev).delete()
    session.commit()


    company1 = Company(name="Tech Corp", founding_year=2010)
    company2 = Company(name="Innovate Ltd", founding_year=2015)


    dev1 = Dev(name="Alice")
    dev2 = Dev(name="Bob")


    freebie1 = Freebie(item_name="T-Shirt", value=20, company=company1, dev=dev1)
    freebie2 = Freebie(item_name="Mug", value=10, company=company1, dev=dev2)
    freebie3 = Freebie(item_name="Sticker Pack", value=5, company=company2, dev=dev1)


    session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])
    session.commit()

def print_data():
    print("\nCompanies:")
    for c in session.query(Company).all():
        print(c)

    print("\nDevelopers:")
    for d in session.query(Dev).all():
        print(d)

    print("\nFreebies:")
    for f in session.query(Freebie).all():
        print(f, f.company, f.dev)

if __name__ == "__main__":
    seed_data()
    print_data()

