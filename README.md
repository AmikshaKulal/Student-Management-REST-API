# Student Management REST API

## Project Overview
A REST API developed using Python and FastAPI to manage student records. It supports creating, viewing, updating, and deleting student information using CRUD operations.

## Technologies Used
- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn
- Swagger UI

## Project Structure
```text
StudentManagement API/
├── database.py
├── models.py
├── schemas.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

1. Clone the repository:
```bash
git clone https://github.com/AmikshaKulal/Student-Management-REST-API.git
```

2. Navigate to the project directory:
```bash
cd Student-Management-REST-API
```

3. Create a virtual environment:
```bash
python -m venv .venv
```

4. Activate it in PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

5. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

6. Run the API:
```bash
python -m uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| POST | `/students` | Create a student |
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PUT | `/students/{student_id}` | Update student details |
| DELETE | `/students/{student_id}` | Delete a student |

## Student Data Model
- `id`: Unique student ID (automatically generated)
- `name`: Student name
- `usn`: Unique university seat number
- `email`: Unique email address
- `branch`: Student branch

## Features
- Complete CRUD operations
- SQLite database integration
- Input validation using Pydantic
- Duplicate USN and email checking
- Error handling for missing students
- JSON request and response support
- Interactive API documentation

## API Documentation

After starting the server, open:

http://127.0.0.1:8000/docs

## Author
Amiksha Kulal