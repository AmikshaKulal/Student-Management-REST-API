
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import engine, get_db
from schemas import StudentCreate, StudentResponse

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(
    title="Student Management API",
    description="A REST API to manage student records",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Student Management API"
    }


# 1. CREATE - Add a new student
@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):

    existing_student = db.query(models.Student).filter(
        (models.Student.usn == student.usn) |
        (models.Student.email == student.email)
    ).first()

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="USN or Email already exists"
        )

    new_student = models.Student(**student.model_dump())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# 2. READ - Get all students
@app.get("/students", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):

    students = db.query(models.Student).all()

    return students


# 3. READ - Get student by ID
@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# 4. UPDATE - Update student details
@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    updated_data: StudentCreate,
    db: Session = Depends(get_db)
):

    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    duplicate = db.query(models.Student).filter(
        models.Student.id != student_id,
        (
            (models.Student.usn == updated_data.usn) |
            (models.Student.email == updated_data.email)
        )
    ).first()

    if duplicate:
        raise HTTPException(
            status_code=400,
            detail="USN or Email already exists"
        )

    for key, value in updated_data.model_dump().items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)

    return student


# 5. DELETE - Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }
