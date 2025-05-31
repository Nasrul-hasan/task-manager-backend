# 🔙 Task Manager - Backend (Flask + PostgreSQL)

This is the backend for the Task Manager web application. It is built with **Flask** and uses **PostgreSQL** as the database. The API provides endpoints to manage tasks: create, read, update, and delete (CRUD).

---

## ⚙️ Features

- ✅ Add new tasks  
- 📋 Get all tasks  
- 📝 Update task name or status (e.g., mark as completed)  
- ❌ Delete a task  
- 🌐 Connected with frontend (Next.js)  
- 🚀 Hosted on Render  

---

## 🔗 Live Backend URL

**Base URL:**  
👉 [https://task-manager-backend-p159.onrender.com](https://task-manager-backend-p159.onrender.com)

---

## 📦 API Endpoints

| Method   | Endpoint                 | Description                      |
|----------|--------------------------|----------------------------------|
| `POST`   | `/add_task`              | Add a new task                   |
| `GET`    | `/get_tasks`             | Get all tasks                    |
| `PUT`    | `/update_task/<task_id>` | Update task name or status       |
| `DELETE` | `/delete_task/<task_id>` | Delete a task                    |

---

## 🛠️ Tech Stack

- Python 3  
- Flask  
- Flask-CORS  
- SQLAlchemy  
- PostgreSQL  
- Hosted on Render  

---

## 🗃️ Database Schema

The backend uses a single table named `tasks` with the following structure:

| Column      | Type    | Description                          |
|-------------|---------|--------------------------------------|
| `id`        | Integer | Primary key (auto-increment)         |
| `task_name` | String  | Name or title of the task            |
| `status`    | String  | Task status (e.g., pending/completed)|

---

## 🌐 Frontend

The frontend of this project is built using **Next.js** and communicates with this Flask API.

- 🔗 **Live URL:** [https://task-manager-frontend-git-main-nasrul-hasans-projects.vercel.app](https://task-manager-frontend-git-main-nasrul-hasans-projects.vercel.app)  
- 📁 **Frontend GitHub Repo:** [https://github.com/Nasrul-hasan/task-manager-frontend](https://github.com/Nasrul-hasan/task-manager-frontend)

---

## 🧪 How to Run Locally

### Prerequisites:

- Python 3.x  
- pip  
- PostgreSQL installed & running  

### Steps:

```bash
# 1. Clone the repository
git clone https://github.com/Nasrul-hasan/task-manager-backend.git
cd task-manager-backend

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up your database (PostgreSQL) and configure DATABASE_URI in config.py

# 4. Run the Flask app
python app.py
