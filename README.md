# Task 2: Detecting Data Leaks Using SQL Injection Protection

## 🔐 Description
This project demonstrates a secure cloud system that protects user data from SQL injection attacks using AES-256 encryption, a capability code mechanism, and a two-layer security protocol.

## ✅ Features
- Cloud-based REST API using Flask
- AES-256 encryption for secure data storage
- Capability code mechanism for authorized SQL operations
- Secure SQL queries using parameterized queries (SQLite)
- Deployed using simple local server or over internet

## 🚀 Setup Instructions
1. Install dependencies:
```
pip install flask pycryptodome
```

2. Run the server:
```
python main.py
```

3. Send requests via Postman or CURL:
- Add User:
```
POST /add_user
{
  "code": "secure123",
  "username": "admin",
  "password": "mypassword"
}
```
- Get Users:
```
GET /get_users
```

## 📌 Notes
- Set environment variable `AES_KEY` for production
- Change `CAPABILITY_CODE` for higher security