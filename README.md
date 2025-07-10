# 🏠 Real Estate Platform - Django REST API

A scalable real estate listing and inquiry platform built with **Django REST Framework**.  Users can browse properties, submit inquiries, favorite listings, and agents/admins can manage content securely.
**Frontend:** [Demo Website](https://altara-homes.vercel.app/)

**Live API:** [API Demo](https://real-estate-backend-ur4i.onrender.com)

---

## 📦 Features

- 🔐 JWT Authentication with login and registration
- 🏘️ Property listings with search & filters
- 📤 Submit and manage inquiries
- ❤️ Favorite/unfavorite properties
- 👮 Admin endpoints to manage users and view stats
- 🐳 Dockerized for production use

---

#  Getting Started

This guide helps you set up the **Real Estate Django REST API** on your local machine for development and testing. You can run it using either **local setup** or **Docker**.

---

## 📁 Prerequisites

- Python 3.10+
- PostgreSQL (or change to SQLite for local testing)
- pip (Python package manager)
- Docker (optional, for containerized setup)

---

##  1. Clone the Repository

```bash
git clone https://github.com/your-username/real-estate-backend.git
cd real-estate-backend
```
##  2. Create a Virtual Environment (Without Docker)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
###   Install Dependencies

```bash
pip install -r requirements.txt
``` 

###   Configure Environment Variables
Create a `.env` file in the project root and add the following variables:
```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1  # Add your domain if deploying
DATABASE_URL=postgres://user:password@localhost:5432/real_estate_db
DB_USER=your_db_user
DB_NAME=your_db_name
DB_PASSWORD=1234
DB_HOST=your_db_host
DB_PORT=5432
DEBUG=False  #True for development, False for production
```

###  Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser
```bash
python manage.py createsuperuser
```

### Run the Development Server
```bash
python manage.py runserver
```

##  3. Docker Setup (Recommended)

###  Build the Docker Image
Make sure you have Docker installed and running. Then build the image:
```bash
docker build -t real-estate-backend .
```

###  Run the Docker Container
You can run the container with the following command:
```bash
docker run -d -p 8000:8000 --env-file .env real-estate-backend
```

## 4. Access the API
Open your browser or API client and navigate to:
```
http://localhost:8000/api/
```
## 5. Admin Interface
Access the Django admin interface at:
```
http://localhost:8000/admin/       
```
Use the superuser credentials you created earlier to log in.    

## 6. API Endpoints
 Django Admin at /admin/ (login with superuser)
 
| Method | Endpoint          | Description                 |
| ------ | ----------------- | --------------------------- |
| POST   | `/register/`      | Register a new user         |
| POST   | `/token/`         | Obtain access & refresh JWT |
| POST   | `/token/refresh/` | Refresh access token        |
| GET    | `/properties/`    | List all properties         |
| GET    | `/properties/<id>/` | Get property details       |
| POST   | `/properties/`    | Create a new property       |
| PUT    | `/properties/<id>/` | Update a property         |
| DELETE | `/properties/<id>/` | Delete a property         |
| GET    | `/inquiries/`     | List all inquiries          |
| POST   | `/inquiries/`     | Submit a new inquiry        |

