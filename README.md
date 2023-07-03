# Identity Reconciliation

This Django project serves as an API for FluxKart.

Use the bellow end point.
http://3.108.219.53/identify

My Resume Link:
https://github.com/midhunpaini/fluxkart/blob/master/fluxkart/resume.pdf

## Tech stacks ##
# Django
# Rest framework
# PostgreSQL
# AWS Ec2 instance
# NGINX
# github



## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (version 3.10.7)
- Django (version 4.2.2)

### Installation

1. Clone the repository:

git clone https://github.com/midhunpaini/fluxkart.git


2. Change into the project directory:

cd fluxkart/fluxkart


3. Create a virtual environment:

python -m venv env


4. Activate the virtual environment:

- On macOS and Linux:

source env/bin/activate


- On Windows:

env\Scripts\activate

5. Creating a new django SECRET_KEY:

Open a terminal or command prompt.

Navigate to the root directory of your Django app.

Run the Python interactive shell by typing python or python3 followed by Enter.

from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()

print(secret_key)

Copy the generated secret key.

Save the secret_key


6. Creating .env files

Create a file named .env inside project directory.

Add the following contents to the .env file, replacing the placeholders with your actual data:

SECRET_KEY=django_secret_key
DATABASE_NAME=your_data_base_name
DATABASE_USER=your_data_user
DATABASE_PASS=your_data_password



7. Install the project dependencies:

pip install -r requirements.txt


8. Run database migrations:

python manage.py makemigrations
python manage.py migrate


9. Start the development server:

python manage.py runserver


10. Access the application:

http://localhost:8000/



