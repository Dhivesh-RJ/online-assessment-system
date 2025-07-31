# 🧠 Online Assessment System (Django Project)

A simple web-based **Online Assessment System** built using Django. This platform enables educators to create subjects, add questions, conduct multiple-choice tests, and record/display student results.

---

## 🚀 Features

- Add multiple subjects (e.g., Math, English)
- Add multiple-choice questions with correct answers
- Create tests and assign questions
- Students can:
  - View available tests
  - Take a test
  - View their results after submission
- Store and display all past results
- Admin interface for managing all data

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite3 (Django default)
- **Frontend:** HTML + Bootstrap (optional for styling)
- **Admin:** Django Admin Panel

---

## 📁 Folder Structure
online-assessment-system/
├── manage.py
├── db.sqlite3
├── README.md
├── .gitignore
├── requirements.txt (optional)
├── online_test/
│ ├── migrations/
│ ├── templates/
│ │ ├── test_list.html
│ │ ├── take_test.html
│ │ └── result.html
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
├── online_assessment_system/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py

yaml
Copy
Edit

---

## ⚙️ Getting Started

### 🔧 Step-by-Step Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/online-assessment-system.git
cd online-assessment-system
Create a virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
Install Django

bash
Copy
Edit
pip install django
Run migrations

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Create a superuser (admin)

bash
Copy
Edit
python manage.py createsuperuser
# Enter username, email (optional), and password
Start the Django development server

bash
Copy
Edit
python manage.py runserver
Open in browser

Admin Panel: http://127.0.0.1:8000/admin

Test List Page: http://127.0.0.1:8000/

📌 Pages Overview
/admin → Admin page to manage subjects, questions, tests, results

/ → Homepage with list of available tests

/test/<id> → Take a specific test

/submit/ → Submit test and view result

/results/ → View past results (if implemented)

📄 .gitignore
Create a .gitignore file in your root project folder and paste this:

markdown
Copy
Edit
venv/
__pycache__/
db.sqlite3
*.pyc
*.pyo
*.pyd
*.sqlite3
*.log
.env
.DS_Store
*.idea/
📸 Screenshots (Add later)
 Admin Panel showing Subjects & Questions

 Student test interface

 Result display screen

📝 Optional Future Enhancements
✅ Display all past results

✅ Prevent re-attempt of same test

✅ Track timestamp of submission

 Add student login system

 Export results as CSV/PDF

 Add Bootstrap for improved UI

 Deploy to cloud (Render, Heroku, etc.)

🙋‍♂️ Developed By
Dhivesh RJ
Built as part of a portfolio project to showcase Django skills in EdTech domain.

📜 License
This project is free to use for educational or non-commercial purposes.
