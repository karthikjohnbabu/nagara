from fastapi import FastAPI, Depends, UploadFile, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import shutil
import os
from datetime import datetime
from uuid import uuid4

from . import models, schemas  # ✅ Make sure this line is there
from .db import SessionLocal


app = FastAPI()

# 👇 Mount uploads folder for public access
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/categories/", response_model=list[schemas.CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()


@app.get("/api/issues/", response_model=list[schemas.IssueList])
def list_issues(db: Session = Depends(get_db)):
    return db.query(models.Issue).order_by(models.Issue.created_at.desc()).all()

@app.get("/api/issues/{issue_id}", response_model=schemas.IssueList)
def get_issue(issue_id: int, db: Session = Depends(get_db)):
    issue = db.query(models.Issue).filter(models.Issue.id == issue_id).first()
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issue



@app.post("/api/issues/", response_model=schemas.IssueResponse)
async def create_issue_with_photo(
    title: str = Form(...),
    description: str = Form(...),
    category_id: int = Form(...),
    latitude: float = Form(None),
    longitude: float = Form(None),
    photo: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    photo_filename = None

    if photo:
        # Rename file with timestamp + UUID to avoid name collisions
        ext = photo.filename.split(".")[-1]
        unique_name = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{uuid4().hex}.{ext}"
        file_location = f"{UPLOAD_DIR}/{unique_name}"

        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(photo.file, buffer)

        # Public URL path
        photo_filename = f"/uploads/{unique_name}"

    db_issue = models.Issue(
        title=title,
        description=description,
        category_id=category_id,
        latitude=latitude,
        longitude=longitude,
        photo=photo_filename,
        status="new"
    )
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue