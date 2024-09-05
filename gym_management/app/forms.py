from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired

class ScheduleForm(FlaskForm):
    """
    Form for adding or editing a schedule.

    Fields:
    - trainer_id: The ID of the trainer for this schedule.
    - date: The date of the schedule.
    - time: The time of the schedule.
    - submit: Submit button for the form.
    """
    trainer_id = IntegerField('Trainer ID', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField('Time', format='%H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Submit')

class MembershipForm(FlaskForm):
    """
    Form for adding or editing a membership.

    Fields:
    - membership_type: The type of the membership.
    - price: The price of the membership.
    - membership_name: The name of the membership.
    - submit: Submit button for the form.
    """
    membership_type = StringField('Membership Type', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    membership_name = StringField('Membership Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class GroupTrainerForm(FlaskForm):
    """
    Form for adding or editing a group training session.

    Fields:
    - trainer_id: The ID of the trainer for this group session.
    - schedule_id: The ID of the schedule for this group session.
    - group_name: The name of the group training session.
    - duration: The duration of the group training session.
    - price: The price of the group training session.
    - submit: Submit button for the form.
    """
    trainer_id = StringField('Trainer ID', validators=[DataRequired()])
    schedule_id = StringField('Schedule ID', validators=[DataRequired()])
    group_name = StringField('Group Name', validators=[DataRequired()])
    duration = FloatField('Duration', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')
