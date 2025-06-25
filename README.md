# 📝 TODO

A simple and intuitive ToDo web application built using **Python** and **Django**. This app allows users to manage their daily tasks efficiently — create tasks, mark them complete/incomplete, update details, and delete when done.

---

## 🚀 Features

- ✅ Add new tasks
- ✏️ Update task details
- 🗑️ Delete tasks
- 📋 Mark tasks as complete/incomplete
- 📆 Due date support
- 🔍 Filter tasks by status
- 🧑 User authentication (Login/Signup)
- 🖥️ Responsive UI (Optional: add Bootstrap or Tailwind)

---

## 🛠 Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS (optionally Bootstrap/Tailwind)
- **Database:** SQLite (default Django DB)
- **Other:** Django's built-in authentication system

---

## 📂 Project Structure
todo_project/
│
├── todo_app/
│ ├── migrations/
│ ├── templates/
│ │ └── todo_app/
│ │ ├── base.html
│ │ ├── task_list.html
│ │ ├── task_form.html
│ │ └── login.html
│ ├── static/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── forms.py
│
├── todo_project/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── db.sqlite3
└── manage.py
