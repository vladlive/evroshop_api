import logging
import os
import shutil
from pathlib import Path
from typing import List
import aiofiles

from fastapi import APIRouter, Depends, HTTPException, UploadFile, status

from models.user import User, UserCreate, UserUpdate
from services.user import UserService

router = APIRouter(
    prefix='/user'
)


@router.get('/', response_model=List[User])
async def get_users(
        service: UserService = Depends()
):
    return await service.get_list()


@router.post('/', response_model=User)
async def create_user(
        user_data: UserCreate,
        service: UserService = Depends()
):
    return await service.create(user_data)


@router.get('/{user_id}', response_model=User)
async def get_user(
        user_id: int,
        service: UserService = Depends()
):
    return await service.get(user_id)


@router.put('/{user_id}', response_model=User)
async def update_user(
    user_id: int,
    user_data: UserUpdate,
    service: UserService = Depends()
):
    return await service.update(
        user_id,
        user_data
    )

@router.post('/avatar_upload')

async def upload_avatar(file: UploadFile):
    destination_file_path = "./theme/assets/images/users/"+file.filename # location to store
    async with aiofiles.open(destination_file_path, 'wb') as out_file:
        while content := await file.read(1024):  # async read file chunk
                await out_file.write(content)  # async write file chunk

    return {'avatar_id': f'{file.filename}', 'status:': True}
