from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telegram_id = db.Column(db.String(50), index=True, unique=True)

    def __repr__(self):
        return '{}'.format(self.telegram_id)
