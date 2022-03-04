from fastapi import APIRouter
#from routers import users
router = APIRouter()


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}
