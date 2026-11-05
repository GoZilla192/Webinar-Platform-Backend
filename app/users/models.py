from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base_model import Base


class User(Base):
	__tablename__ = "users"
	
	id: Mapped[int] = mapped_column(
		autoincrement=True, primary_key=True
	)
	email: Mapped[str] = mapped_column(nullable=False, unique=True)
	password: Mapped[str] = mapped_column(nullable=False)
