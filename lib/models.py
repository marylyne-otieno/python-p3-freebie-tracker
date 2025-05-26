
from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)


Base = declarative_base(metadata=metadata)



# Company Model
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())


    @property
    def devs(self):
        return list({freebie.dev for freebie in self.freebies})

    def give_freebie(self, session, dev, item_name, value):
        """Create a new Freebie for a dev from this company."""
        freebie = Freebie(item_name=item_name, value=value, company=self, dev=dev)
        session.add(freebie)
        session.commit()

    @classmethod
    def oldest_company(cls, session):
        """Return the company with the earliest founding year."""
        return session.query(cls).order_by(cls.founding_year).first()

    def __repr__(self):
        return f'<Company {self.name}>'


# Dev Model

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    @property
    def companies(self):
        return list({freebie.company for freebie in self.freebies})

    def received_one(self, item_name):
        """Check if dev received a freebie with the given item name."""
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, session, other_dev, freebie):
        """Transfer a freebie to another dev, only if this dev owns it."""
        if freebie.dev_id == self.id:
            freebie.dev = other_dev
            session.commit()

    def __repr__(self):
        return f'<Dev {self.name}>'



# Freebie Model

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())

    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    company = relationship("Company", backref=backref("freebies", cascade="all, delete-orphan"))
    dev = relationship("Dev", backref=backref("freebies", cascade="all, delete-orphan"))

    def print_details(self):
        """Return a string describing the freebie, its dev, and company."""
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"

    def __repr__(self):
        return f'<Freebie {self.item_name} | ${self.value}>'
