from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired

class ScheduleForm(FlaskForm):
    trainer_id = IntegerField('Trainer ID', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField('Time', format='%H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Submit')

class MembershipForm(FlaskForm):
    membership_type = StringField('Membership Type', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    membership_name = StringField('Membership Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class GroupTrainerForm(FlaskForm):
    trainer_id = IntegerField('Trainer ID', validators=[DataRequired()])
    schedule_id = IntegerField('Schedule ID', validators=[DataRequired()])
    group_name = StringField('Group Name', validators=[DataRequired()])
    duration = IntegerField('Duration (minutes)', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')
