from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Trainer, Client, Schedule, Membership, GroupTrainer
from app.forms import ScheduleForm, MembershipForm, GroupTrainerForm

# List of Trainers
@app.route('/trainers')
def trainers():
    """
    Render a list of all trainers.
    """
    trainers = Trainer.query.all()
    for trainer in trainers:
        print(f"Trainer: {trainer.first_name} {trainer.last_name}, ID: {trainer.trainer_id}")
    return render_template('trainers/trainers.html', trainers=trainers)

# Trainer Detail
@app.route('/trainers/<int:trainer_id>')
def trainer_detail(trainer_id):
    """
    Render details of a specific trainer identified by trainer_id.
    """
    trainer = Trainer.query.get_or_404(trainer_id)
    return render_template('trainers/trainer_detail.html', trainer=trainer)

# Add New Trainer
@app.route('/trainers/add', methods=['GET', 'POST'])
def add_trainer():
    """
    Add a new trainer to the database. Displays form on GET request and processes form data on POST request.
    """
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        email = request.form['email']
        phone = request.form.get('phone', '')
        license_number = request.form.get('license_number', '')
        license_expiry = request.form.get('license_expiry', None)
        experience = request.form.get('experience', '')
        sport_specialty = request.form.get('sport_specialty', '')

        # Create a new Trainer instance
        new_trainer = Trainer(
            first_name=first_name,
            last_name=last_name,
            age=age,
            email=email,
            phone=phone,
            license_number=license_number,
            license_expiry=license_expiry,
            experience=experience,
            sport_specialty=sport_specialty
        )

        # Add and commit the new trainer to the database
        db.session.add(new_trainer)
        db.session.commit()

        return redirect(url_for('trainers'))

    return render_template('trainers/add_trainer.html')

# Edit Trainer
@app.route('/trainers/edit/<int:trainer_id>', methods=['GET', 'POST'])
def edit_trainer(trainer_id):
    """
    Edit an existing trainer identified by trainer_id. Displays form on GET request and updates trainer details on POST request.
    """
    trainer = Trainer.query.get_or_404(trainer_id)
    if request.method == 'POST':
        trainer.first_name = request.form['first_name']
        trainer.last_name = request.form['last_name']
        trainer.age = request.form['age']
        trainer.email = request.form['email']
        trainer.phone = request.form['phone']
        trainer.license_number = request.form['license_number']
        trainer.license_expiry = request.form['license_expiry']
        trainer.experience = request.form['experience']
        trainer.sport_specialty = request.form['sport_specialty']
        db.session.commit()
        flash('Trainer updated successfully!')
        return redirect(url_for('trainers'))
    return render_template('trainers/edit_trainer.html', trainer=trainer)

# Delete Trainer
@app.route('/trainers/delete/<int:trainer_id>', methods=['POST'])
def delete_trainer(trainer_id):
    """
    Delete a trainer identified by trainer_id from the database.
    """
    trainer = Trainer.query.get_or_404(trainer_id)
    db.session.delete(trainer)
    db.session.commit()
    flash('Trainer deleted successfully!')
    return redirect(url_for('trainers'))

# List of Clients
@app.route('/clients')
def clients():
    """
    Render a list of all clients.
    """
    clients = Client.query.all()
    return render_template('clients/clients.html', clients=clients)

@app.route('/clients/<int:client_id>')
def client_detail(client_id):
    """
    Render details of a specific client identified by client_id.
    """
    client = Client.query.get_or_404(client_id)
    return render_template('clients/client_detail.html', client=client)

@app.route('/clients')
def show_clients():
    """
    Display a list of all clients.
    """
    clients = Client.query.all()
    return render_template('clients/clients.html', clients=clients)

@app.route('/clients/add', methods=['GET', 'POST'])
def add_client():
    """
    Add a new client to the database. Displays form on GET request and processes form data on POST request.
    """
    if request.method == 'POST':
        new_client = Client(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            age=request.form['age'],
            email=request.form['email'],
            phone=request.form['phone'],
            member_number=request.form['member_number'],
            join_date=request.form['join_date'],
            address=request.form['address'],
            membership_id=request.form['membership_id'],
            group_training_id=request.form['group_training_id'],
            start_date=request.form['start_date'],
            end_date=request.form['end_date']
        )
        db.session.add(new_client)
        db.session.commit()
        flash('Client added successfully!')
        return redirect(url_for('clients'))
    return render_template('clients/add_client.html')

# Edit Client
@app.route('/clients/edit/<int:client_id>', methods=['GET', 'POST'])
def edit_client(client_id):
    """
    Edit an existing client identified by client_id. Displays form on GET request and updates client details on POST request.
    """
    client = Client.query.get_or_404(client_id)
    if request.method == 'POST':
        client.first_name = request.form['first_name']
        client.last_name = request.form['last_name']
        client.age = request.form['age']
        client.email = request.form['email']
        client.phone = request.form['phone']
        client.member_number = request.form['member_number']
        client.join_date = request.form['join_date']
        client.address = request.form['address']
        client.membership_id = request.form['membership_id']
        client.group_training_id = request.form['group_training_id']
        client.start_date = request.form['start_date']
        client.end_date = request.form['end_date']
        db.session.commit()
        flash('Client updated successfully!')
        return redirect(url_for('clients'))
    return render_template('clients/edit_client.html', client=client)

@app.route('/clients/delete/<int:client_id>', methods=['POST'])
def delete_client(client_id):
    """
    Delete a client identified by client_id from the database.
    """
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    flash('Client deleted successfully!')
    return redirect(url_for('clients'))

# Show Schedule
@app.route('/schedule')
def show_schedule():
    """
    Render a list of all schedules.
    """
    schedules = Schedule.query.all()
    return render_template('schedule/schedule.html', schedules=schedules)

# Add Schedule
@app.route('/schedule/add', methods=['GET', 'POST'])
def add_schedule():
    """
    Add a new schedule to the database. Displays form on GET request and processes form data on POST request.
    """
    form = ScheduleForm()
    if form.validate_on_submit():
        new_schedule = Schedule(
            trainer_id=form.trainer_id.data,
            date=form.date.data,
            time=form.time.data
        )
        db.session.add(new_schedule)
        db.session.commit()
        flash('Schedule added successfully!')
        return redirect(url_for('show_schedule'))
    return render_template('schedule/add_schedule.html', form=form)

# Edit Schedule
@app.route('/schedule/edit/<int:schedule_id>', methods=['GET', 'POST'])
def edit_schedule(schedule_id):
    """
    Edit an existing schedule identified by schedule_id. Displays form on GET request and updates schedule details on POST request.
    """
    schedule = Schedule.query.get_or_404(schedule_id)
    form = ScheduleForm(obj=schedule)
    if form.validate_on_submit():
        schedule.trainer_id = form.trainer_id.data
        schedule.date = form.date.data
        schedule.time = form.time.data
        db.session.commit()
        flash('Schedule updated successfully!')
        return redirect(url_for('show_schedule'))
    return render_template('schedule/edit_schedule.html', form=form)

# Delete Schedule
@app.route('/schedule/delete/<int:schedule_id>', methods=['POST'])
def delete_schedule(schedule_id):
    """
    Delete a schedule identified by schedule_id from the database.
    """
    schedule = Schedule.query.get_or_404(schedule_id)
    db.session.delete(schedule)
    db.session.commit()
    flash('Schedule deleted successfully!')
    return redirect(url_for('show_schedule'))

@app.route('/memberships')
def memberships():
    """
    Render a list of all memberships.
    """
    memberships = Membership.query.all()
    return render_template('membership/memberships.html', memberships=memberships)

# Add Membership
@app.route('/memberships/add', methods=['GET', 'POST'])
def add_membership():
    """
    Add a new membership to the database. Displays form on GET request and processes form data on POST request.
    """
    form = MembershipForm()
    if form.validate_on_submit():
        new_membership = Membership(
            membership_type=form.membership_type.data,
            price=form.price.data,
            membership_name=form.membership_name.data
        )
        db.session.add(new_membership)
        db.session.commit()
        flash('Membership added successfully!')
        return redirect(url_for('memberships'))
    return render_template('membership/add_membership.html', form=form)

# Edit Membership
@app.route('/memberships/edit/<int:membership_id>', methods=['GET', 'POST'])
def edit_membership(membership_id):
    """
    Edit an existing membership identified by membership_id. Displays form on GET request and updates membership details on POST request.
    """
    membership = Membership.query.get_or_404(membership_id)
    form = MembershipForm(obj=membership)
    if form.validate_on_submit():
        membership.membership_type = form.membership_type.data
        membership.price = form.price.data
        membership.membership_name = form.membership_name.data
        db.session.commit()
        flash('Membership updated successfully!')
        return redirect(url_for('memberships'))
    return render_template('membership/edit_membership.html', form=form, membership=membership)

# Delete Membership
@app.route('/memberships/delete/<int:membership_id>', methods=['POST'])
def delete_membership(membership_id):
    """
    Delete a membership identified by membership_id from the database.
    """
    membership = Membership.query.get_or_404(membership_id)
    db.session.delete(membership)
    db.session.commit()
    flash('Membership deleted successfully!')
    return redirect(url_for('memberships'))

# List of Group Trainers
@app.route('/group_trainer')
def group_trainer():
    """
    Render a list of all group trainers.
    """
    group_trainer_list = get_group_trainers()
    return render_template('grouptrainer/group_trainer.html', group_trainer=group_trainer_list)

def get_group_trainers():
    """
    Retrieve a list of all group trainers.
    """
    return db.session.query(GroupTrainer).all()

# Edit Group Trainer
@app.route('/group_trainer/edit/<int:group_trainer_id>', methods=['GET', 'POST'])
def edit_group_trainer(group_trainer_id):
    """
    Edit an existing group trainer identified by group_trainer_id. Displays form on GET request and updates trainer details on POST request.
    """
    group_trainer = GroupTrainer.query.get_or_404(group_trainer_id)
    form = GroupTrainerForm(obj=group_trainer)
    if form.validate_on_submit():
        group_trainer.trainer_id = form.trainer_id.data
        group_trainer.schedule_id = form.schedule_id.data
        group_trainer.group_name = form.group_name.data
        group_trainer.duration = form.duration.data
        group_trainer.price = form.price.data
        db.session.commit()
        flash('Group Trainer updated successfully!')
        return redirect(url_for('group_trainer'))
    return render_template('grouptrainer/edit_group_trainer.html', form=form)

# Add Group Trainer
@app.route('/group_trainer/add', methods=['GET', 'POST'])
def add_group_trainer():
    """
    Add a new group trainer to the database. Displays form on GET request and processes form data on POST request.
    """
    form = GroupTrainerForm()
    if form.validate_on_submit():
        new_group_trainer = GroupTrainer(
            trainer_id=form.trainer_id.data,
            schedule_id=form.schedule_id.data,
            group_name=form.group_name.data,
            duration=form.duration.data,
            price=form.price.data
        )
        db.session.add(new_group_trainer)
        db.session.commit()
        flash('Group Trainer added successfully!')
        return redirect(url_for('group_trainer'))
    return render_template('grouptrainer/add_group_trainer.html', form=form)

# Delete Group Trainer
@app.route('/group_trainer/delete/<int:group_trainer_id>', methods=['POST'])
def delete_group_trainer(group_trainer_id):
    """
    Delete a group trainer identified by group_trainer_id from the database.
    """
    group_trainer = GroupTrainer.query.get_or_404(group_trainer_id)
    db.session.delete(group_trainer)
    db.session.commit()
    flash('Group Trainer deleted successfully!')
    return redirect(url_for('group_trainer'))

# Home Page
@app.route('/')
def index():
    """
    Render the home page.
    """
    return render_template('index.html')

# Home Page (Alternative)
@app.route('/home')
def home():
    """
    Render the home page alternative.
    """
    return render_template('home.html')

@app.route('/schedule')
def schedule():
    """
    Render the schedule page.
    """
    return render_template('schedule.html')

@app.route('/readme')
def readme():
    """
    Render the readme page.
    """
    return render_template('readme.html')

@app.route('/membership')
def membership():
    """
    Render the memberships page.
    """
    return render_template('membership/memberships.html')

@app.route('/purchase_group_training', methods=['POST'])
def purchase_group_training():
    """
    Handle the purchase of a group training session. Retrieves form data
    and redirects to the menu page.
    """
    membership = request.form.get('membership')
    trainer = request.form.get('trainer')
    schedule = request.form.get('schedule')
    return redirect(url_for('menu'))

@app.route('/view_details')
def view_details():
    """
    Render a page displaying details of all group trainers.
    """
    group_trainers = GroupTrainer.query.all()
    return render_template('details.html', group_trainers=group_trainers)

@app.route('/menu')
def menu():
    """
    Render the menu page.
    """
    return render_template('menu.html')


