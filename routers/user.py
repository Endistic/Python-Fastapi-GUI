from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid
router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"message": "Not found"}}
)

# New
user_db = []


class User(BaseModel):
    id: Optional[str]
    name: str
    age: str
    info: Text
    create_at: datetime = datetime.now()


@router.get("/read")
async def read_user():
    return user_db


@router.post("/create")
async def create_user(user: User):
    user.id = str(uuid())
    user_db.append(user.dict())
    return user_db[-1]


# @router.get("/getById/{user_id}")
# async def get_userbyId(user_id: str):
#     for user in user_db:
#         if user["id"] == user_id:
#             return user
#     raise HTTPException(status_code=404, detail="Not Found !")
#     # return {"message": "Not Found"}


@router.put("/edit/{id}")
async def edit_userbyId(id: str, userUpdate: User):
    for index, user in enumerate(user_db):
        if user["id"] == id:
            user_db[index]["name"] = userUpdate.name
            user_db[index]["age"] = userUpdate.age
            user_db[index]["info"] = userUpdate.info
            return {"message": " Update successfully "}
    raise HTTPException(status_code=404, detail="Not Found !")


@router.delete("/delete/{id}")
async def delete_userbyId(id: str):
    print(id)
    for index, user in enumerate(user_db):
        print(user)
        if user['id'] == id:
            user_db.pop(index)
            return {"message": user_db}
        raise HTTPException(status_code=404, detail="Not Found !")