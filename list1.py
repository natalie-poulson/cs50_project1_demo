import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = Flight.query.all()
    for flight in flights:
        print(f'{flight.origin} to {flight.destination}, {flight.duration} minutes.')


if __name__ == '__main__':
    with app.app_context():
        main()