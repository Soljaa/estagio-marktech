from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base


database_url = 'sqlite:///./database/university.db'
db = create_engine(database_url)
Base = declarative_base()


class Student(Base):

    __tablename__ = 'student'

    registry = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    degree = Column(String)
    birth_date = Column(Date)

    def to_dict(self):
        return {
            'registry': self.registry,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'degree': self.degree,
            'birth_date': str(self.birth_date)
        }


def create_db():
    Base.metadata.create_all(db)


if __name__ == '__main__':
    create_db()
