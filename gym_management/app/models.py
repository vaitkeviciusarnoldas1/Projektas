from app import db

class Trainer(db.Model):
    """Model representing a trainer in the system."""
    __tablename__ = 'trainers'

    trainer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    license_number = db.Column(db.String(50))
    license_expiry = db.Column(db.Date)
    experience = db.Column(db.String(100))
    sport_specialty = db.Column(db.String(100))

    group_trainings = db.relationship('GroupTrainer', back_populates='trainer')

class Client(db.Model):
    """Model representing a client in the system."""
    __tablename__ = 'clients'

    client_id = db.Column(db.Integer, primary_key=True,)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    member_number = db.Column(db.String(50), unique=True)
    join_date = db.Column(db.Date)
    address = db.Column(db.String(200))
    membership_id = db.Column(db.Integer, db.ForeignKey('memberships.membership_id'))
    group_training_id = db.Column(db.Integer, db.ForeignKey('grouptrainers.group_training_id'))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    membership = db.relationship('Membership', backref='clients')
    group_trainings = db.relationship('GroupTrainer', backref='clients')

class GroupTrainer(db.Model):
    """Model representing a group training session."""
    __tablename__ = 'grouptrainers'

    group_training_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.trainer_id'))
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.schedule_id'))
    group_name = db.Column(db.String(100))
    duration = db.Column(db.String(50))
    price = db.Column(db.Float)

    trainer = db.relationship('Trainer', back_populates='group_trainings')
    schedule = db.relationship('Schedule', back_populates='group_trainings')

class Membership(db.Model):
    """Model representing a membership in the system.

    Attributes:
        membership_id (int): The unique identifier for the membership.
        membership_type (str): The type of the membership.
        price (float): The price of the membership.
        membership_name (str): The name of the membership.
    """
    __tablename__ = 'memberships'

    membership_id = db.Column(db.Integer, primary_key=True)
    membership_type = db.Column(db.String(50))
    price = db.Column(db.Float)
    membership_name = db.Column(db.String(100))

class Schedule(db.Model):
    """Model representing a schedule entry in the system.

    Attributes:
        schedule_id (int): The unique identifier for the schedule entry.
        trainer_id (int): The ID of the trainer associated with the schedule.
        date (date): The date of the schedule.
        time (time): The time of the schedule.

    Relationships:
        group_trainings (relationship): A relationship to the GroupTrainer model, linking schedules to group training sessions.
    """
    __tablename__ = 'schedule'
    schedule_id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)

    group_trainings = db.relationship('GroupTrainer', back_populates='schedule')
