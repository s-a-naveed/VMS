markdown
# Vehicle Management System

Welcome to the Vehicle Management System (VMS) project! This Django-based web application allows users to manage vehicle details and quality checks efficiently.

## Features

- User authentication: Users can register, log in, and log out securely.
- Vehicle management: Users can add, view, edit, and delete vehicle details.
- Quality checks: Users can perform quality checks on vehicles and update their status.

## Running the Project

To run this project locally, follow these steps:

1. Clone the repository to your local machine:

   bash
   git clone https://github.com/s-a-naveed/V_M_S.git
   

2. Navigate to the project directory:

   bash
   cd vehicle-management-system
   

3. Install the required dependencies:

   bash
   pip install -r requirements.txt
   

4. Apply migrations to set up the database:

   bash
   python manage.py migrate
   

5. Start the development server:

   bash
   python manage.py runserver
   

6. Access the application in your web browser at `http://127.0.0.1:8000`.

## Performing Migrations

If you make changes to the models or database schema, you'll need to perform migrations. Follow these steps:

1. Make changes to your models in `models.py`.

2. Generate migration files:

   bash
   python manage.py makemigrations
   

3. Apply the migrations:

   bash
   python manage.py migrate
   ```

## Usage

1. Register an account or log in if you already have one.

2. Navigate to the "Vehicles" section to manage vehicle details.

3. Perform quality checks on vehicles in the "Quality Checks" section.

4. Edit vehicle quality checks as needed.
