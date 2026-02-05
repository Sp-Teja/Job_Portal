"# JobPortal_BackEnd" 
# 🧑‍💻 Job Portal Backend (Django + DRF)

A fully functional **Job Portal Backend** built using **Django & Django REST Framework (DRF)**.  
It enables companies to post jobs, and users to apply for them using JWT Authentication.

---

## 🚀 Features
- User Registration & Login (JWT)
- Job CRUD (Create, List, Update, Delete)
- Apply for Jobs
- Filtering (title & location)
- Pagination
- Clean DRF architecture (Models → Serializers → Views → URLs)

---

## 🏗 Tech Stack
- Python
- Django 5
- Django REST Framework
- MySQL
- Simple JWT Authentication

---

## 📌 API Endpoints

### 🔐 Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register/` | Register User |
| POST | `/auth/login/` | Login and get JWT tokens |

---

### 💼 Jobs
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/jobs/list/` | List all jobs |
| POST | `/jobs/create/` | Create a job |
| PUT | `/jobs/update/<id>/` | Update job |
| DELETE | `/jobs/delete/<id>/` | Delete job |

---

### 📝 Job Applications
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/jobs/apply/<id>/` | Apply for a job |

---

## 🗂 Folder Structure
