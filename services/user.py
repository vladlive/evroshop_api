from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

import tables
from database import get_session
from models.user import UserCreate, UserUpdate


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, u_id: int) -> tables.User:
        user = (
            self.session
            .query(tables.User)
            .filter_by(id=u_id)
            .first()
        )
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user

    def get(self, u_id: int) -> tables.User:
        return self._get(u_id)

    def get_list(self) -> List[tables.User]:
        user = (
            self.session.query(tables.User).all()
        )
        return user

    def create(self, user_data: UserCreate) -> tables.User:
        user = tables.User(**user_data.dict())
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, u_id: int, user_data: UserUpdate) -> tables.User:
        user = self._get(u_id)
        for field, value in user_data:
            setattr(user, field, value)
        self.session.commit()
        return user
