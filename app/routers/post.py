from typing import List

from fastapi import APIRouter,HTTPException
from app.schemas import BlogPostCreate, CategoryCreate

router = APIRouter()
CATEGORIES = []

@router.post("/update-category", response_model=List[str])
async def add_category(category: CategoryCreate):
    name = category.name.strip().lower()

    if not name:
        raise HTTPException(status_code=400, detail="Category name cannot be empty.")

    if name in CATEGORIES:
        raise HTTPException(status_code=400, detail="Category already exists.")

    CATEGORIES.append(name)
    return CATEGORIES

@router.post("/upload-post")
async def upload_post(payload: BlogPostCreate):
    print({
        "title": payload.title,
        "slug": payload.slug,
        "category": payload.category,
        "content": payload.content_json
    })
    return {
        "title": payload.title,
        "slug": payload.slug,
        "category": payload.category,
        "content": payload.content_json
    }