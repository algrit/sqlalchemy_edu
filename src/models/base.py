from typing import Annotated
import enum

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

pk_int = Annotated[int, mapped_column(primary_key=True)]

class Sex(enum.Enum):
    m = "male"
    f = "female"
    x = "other"


class PersonORM(Base):
    id: Mapped[pk_int]
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    sex: Mapped[Sex]


class WorkerORM(Base):
    id: Mapped[pk_int]
    person_id: Mapped[int] = mapped_column(ForeignKey=PersonORM.id)
