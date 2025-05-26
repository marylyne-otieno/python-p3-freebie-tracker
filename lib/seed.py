#!/usr/bin/env python3

# Script goes here!
from models import Company, Dev, Freebie, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

company1 = Company(name="Google", founding_year=1998)
company2 = Company(name="Amazon", founding_year=1994)
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

session.add_all([company1, company2, dev1, dev2])
session.commit()

company1.give_freebie(session, dev1, "T-shirt", 15)
company2.give_freebie(session, dev2, "Mug", 10)
session.commit()

