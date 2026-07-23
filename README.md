# User Authentication API

A RESTful User Authentication API built with Flask, MySQL, and JWT Authentication. This project provides secure user registration, login, and profile access using JSON Web Tokens (JWT).

---

## 🚀 Features

- User Registration
- User Login
- Password Hashing
- JWT Authentication
- Protected Profile API
- Input Validation
- MySQL Database
- Environment Variables using `.env`

---

## 🛠️ Technologies Used

- Python
- Flask
- MySQL
- Flask-JWT-Extended
- Werkzeug
- python-dotenv

---

## 📁 Project Structure

```
user_authentication/
│── app.py
│── db.py
│── user_routes.py
│── validations.py
│── login.py
│── register.py
│── requirements.txt
│── .gitignore
│── README.md
│── .env (Not uploaded)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/user_authentication.git
```

### 2. Move into the project

```bash
cd user_authentication
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=user_authentication

JWT_SECRET_KEY=your_secret_key
```

### 7. Run the application

```bash
python app.py
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/users` | Register a new user |
| POST | `/login` | Login user |
| GET | `/profile` | Get logged-in user profile |

---

## 🔒 Authentication

Protected APIs require a JWT Access Token.

Example:

```
Authorization: Bearer <your_access_token>
```

---

## 📦 Requirements

Install all required packages using:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

Tarun Sai Kumar