# CRM Project

This project is a Customer Relationship Management (CRM) system built using Python, Django, MySQL, HTML, and Tailwind CSS. It provides functionalities for managing client details, user authentication, and CRUD operations on records.

## Features

- **User Authentication:** Allows users to sign up, log in, and log out securely.
- **Record Management:** Users can add, modify, and delete client records.
- **Responsive Design:** Built with HTML and styled with Tailwind CSS for a modern and responsive UI.

## Getting Started

To run this project locally, follow these steps:

### Prerequisites

- Python (version 3.x)
- Django
- MySQL (or another relational database)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/crm-project.git
   cd crm-project
2. Install Python dependencies:
     pip install -r requirements.txt
3. Set up the database:
  - Create a MySQL database named crm.
  - Configure the database settings in settings.py:
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'crm',
              'USER': 'your_database_user',
              'PASSWORD': 'your_database_password',
              'HOST': 'localhost',
              'PORT': '3306',
          }
      }
4. Apply database migrations:
    ```bash
      python manage.py migrate

5. Run the development server:
     ```bash
      python manage.py runserver
6. Access the CRM application at `http://localhost:8000` in your web browser.

## Contributing
  Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.
## Note
   Replace placeholders like `your-username`, `your_database_user`, and `your_database_password` with your actual details before pushing to GitHub. This README.md file provides clear instructions for anyone to set up and use your CRM project locally.)


## Demo Images
![image](https://github.com/CSE21098/Django-CRM/assets/96134058/d938632f-2143-48fc-8110-3525075ad777)
![image](https://github.com/CSE21098/Django-CRM/assets/96134058/52309530-4ec1-448e-b5af-eff78e220ff4)
![image](https://github.com/CSE21098/Django-CRM/assets/96134058/3745168c-e30d-4826-b2cd-0cd6380cad70)
