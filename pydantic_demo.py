from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "John Doe"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default = 5, description="A decimal value representing.")

new_student = {"age": 23, "email": "abc@gmail.com", "cgpa": 10}

student = Student(**new_student)

student_dict = dict(student)
print(student_dict['age'])
student_json = student.model_Dump_json()