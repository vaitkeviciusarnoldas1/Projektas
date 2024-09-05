from app import db

class Trainer(db.Model):
    __tablename__ = 'trainers'  # Patikrinkite ar pavadinimas atitinka jūsų DB lentelės pavadinimą

    trainer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    license_number = db.Column(db.String(50))
    license_expiry = db.Column(db.Date)
    experience = db.Column(db.String(100))
    sport_specialty = db.Column(db.String(50))

    def __repr__(self):
        return f'<Trainer {self.first_name} {self.last_name}>'

class Client(db.Model):
    __tablename__ = 'clients'  # Patikrinkite ar pavadinimas atitinka jūsų DB lentelės pavadinimą

    client_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    member_number = db.Column(db.String(50))
    join_date = db.Column(db.Date)
    address = db.Column(db.String(200))
    membership_id = db.Column(db.Integer)
    group_training_id = db.Column(db.Integer)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    def __repr__(self):
        return f'<Client {self.first_name} {self.last_name}>'
