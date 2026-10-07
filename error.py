from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()
students={
    "S001":{"name":"Ravi",'marks':75,"grade":"B"},
    "S002":{"name":"Sumit",'marks':88,"grade":"A"},
    "S003":{"name":"Khushi",'marks':92,"grade":"A+"}
}
class MarksSubmission(BaseModel):
    student_id:str
    marks:int
    subject:str

@app.get("/students/{student_id}")
def get_student(student_id:str):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail=f"Student with id {student_id} not found"
        )
    return students[student_id]

@app.post("/submit_marks")
def submit_marks(submit:MarksSubmission):
    #C1: Student not found
    if submit.student_id not in students:
        raise HTTPException(
            status_code=404,
            detail=f"Student with id {submit.student_id} not found"
        )
    #C2: valid range 0-100
    if submit.marks <0 or submit.marks>100:
        raise HTTPException(
            status_code=400,
            detail={
                "error":"Invalid marks",
                "marks_received":submit.marks,
                "fix":"Marks should be in the range of 0-100"
            }
        )

    #C3:subject name empty
    if submit.subject.strip()=="":
        raise HTTPException(
            status_code=400,
            detail={
                "error":"Invalid subject name",
                "subject_received":submit.subject,
                "fix":"Subject name should not be empty"
            }
        )
    try:
        students[submit.student_id]['marks']=submit.marks
        return {
        "message":f"Marks for student {submit.student_id} updated successfully",
        "marks":submit.marks,
        "subject":submit.subject
    }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "message":f"Something went wrong from our side {e}"
            }
        )

