from sqlalchemy import MetaData
from app.data_base import db, engine

class DbDefault(object):

    def save(self):
        metadata = MetaData()
        metadata.create_all(engine)
        print 'engine = ', engine
        db.session.add(self)
        db.session.commit()
        return self

    def refresh(self):
        db.session.expire(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def populate(self, values):
        for key, value in values.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)
        return self


class Applicant(db.Model, DbDefault):
    __tablename__ = 'applicants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
