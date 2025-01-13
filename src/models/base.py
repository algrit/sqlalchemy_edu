import enum

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Sex(enum.Enum):
    m = "male"
    f = "female"
    x = "other"


class PersonORM(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    sex: Mapped[Sex]
