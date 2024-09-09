markdown
Copy code
# Gym Management System

## Introduction

Welcome to the Gym Management System, a comprehensive web application for managing gym operations. This system facilitates the management of trainers, clients, schedules, memberships, and group training sessions. Developed using Flask, SQLAlchemy, and PostgreSQL, it offers an intuitive interface to streamline gym management tasks.

## Key Features

- **Trainer Management**: Add, update, view, and delete trainer profiles.
- **Client Management**: Oversee client information, including membership details and group training sessions.
- **Schedule Management**: Create and maintain training schedules.
- **Membership Management**: Manage membership plans, including creation, updates, and deletions.
- **Group Training Management**: Organize and schedule group training sessions, manage session pricing.

## Installation Guide

### Requirements

- Python 3.x
- PostgreSQL (SQLite can be used for development)
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Migrate
- SQLAlchemy

### Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/gym-management-system.git
   cd gym-management-system
2. Create and Activate a Virtual Environment:
   ```bash 
   python -m venv venv source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install Required Dependencies:
   ```bash 
   pip install -r requirements.txt

4. Configure Environment Variables: Create a .env file in the root directory and add your database URL:
   ```bash
   DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/yourdatabase
   
5. Initialize the Database:
   ```bash
   flask db upgrade

6. Run the Application:
   ```bash
   python run.py

The application will be available at http://localhost:5006.

**Application Routes**

Home: /
Trainers: /trainers
Clients: /clients
Schedule: /schedule
Memberships: /memberships
Group Training: /group_trainer

**Diagram**
![Diagram](https://github.com/yourusername/gym-management-system/blob/main/images/diagrama.png)

**Contributing**

To contribute to the project:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature

3. Commit your changes:
   ```bash
   git commit -am 'Add new feature'

4. Push your branch:
   ```bash
   git push origin feature/YourFeature
   
5. Create a Pull Request.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments

Flask - Web framework used.
SQLAlchemy - ORM for database operations.
Flask-WTF - Form handling.
