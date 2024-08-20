from . import db

class Credit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    credit_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def approve(self):
        self.status = 'Success'
        db.session.commit()

    def __repr__(self):
        return f'<Credit {self.client_name}>'
