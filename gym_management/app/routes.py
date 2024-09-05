from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Trainer, Client

# Trenerių sąrašas
@app.route('/trainers')
def trainers():
    trainers = Trainer.query.all()  # Gauti visus trenerius
    return render_template('trainers.html', trainers=trainers)

# Trenerio detalės
@app.route('/trainers/<int:trainer_id>')
def trainer_detail(trainer_id):
    trainer = Trainer.query.get_or_404(trainer_id)
    return render_template('trainer_detail.html', trainer=trainer)

# Naujo trenerio pridėjimas
@app.route('/trainers/add', methods=['GET', 'POST'])
def add_trainer():
    if request.method == 'POST':
        new_trainer = Trainer(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            age=request.form['age'],
            email=request.form['email'],
            phone=request.form['phone'],
            license_number=request.form['license_number'],
            license_expiry=request.form['license_expiry'],
            experience=request.form['experience'],
            sport_specialty=request.form['sport_specialty']
        )
        db.session.add(new_trainer)
        db.session.commit()
        flash('Trainer added successfully!')
        return redirect(url_for('trainers'))
    return render_template('add_trainer.html')

# Trenerio redagavimas
@app.route('/trainers/edit/<int:trainer_id>', methods=['GET', 'POST'])
def edit_trainer(trainer_id):
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
    return render_template('edit_trainer.html', trainer=trainer)

# Trenerio ištrynimas
@app.route('/trainers/delete/<int:trainer_id>', methods=['POST'])
def delete_trainer(trainer_id):
    trainer = Trainer.query.get_or_404(trainer_id)
    db.session.delete(trainer)
    db.session.commit()
    flash('Trainer deleted successfully!')
    return redirect(url_for('trainers'))

# Klientų sąrašas
@app.route('/clients')
def clients():
    clients = Client.query.all()  # Gauti visus klientus
    return render_template('clients.html', clients=clients)

# Kliento detalės
@app.route('/clients/<int:client_id>')
def client_detail(client_id):
    client = Client.query.get_or_404(client_id)
    return render_template('client_detail.html', client=client)

# Naujo kliento pridėjimas
@app.route('/clients/add', methods=['GET', 'POST'])
def add_client():
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
    return render_template('add_client.html')

# Kliento redagavimas
@app.route('/clients/edit/<int:client_id>', methods=['GET', 'POST'])
def edit_client(client_id):
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
    return render_template('edit_client.html', client=client)

# Kliento ištrynimas
@app.route('/clients/delete/<int:client_id>', methods=['POST'])
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    flash('Client deleted successfully!')
    return redirect(url_for('clients'))

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/')
def home():
    return render_template('index.html')