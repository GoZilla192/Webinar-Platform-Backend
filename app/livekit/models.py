import secrets
import string

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from app.infrastructure.database.base_model import Base


def generate_room_id():
	cnt_parts = 4
	len_part = 4
	
	parts = [''] * cnt_parts
	
	for i in range(cnt_parts):
		parts[i] = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(len_part))
	
	return '-'.join(parts)


class Room(Base):
	__tablename__ = "rooms"
	
	room_id: Mapped[str] = mapped_column(
		String(20),
		primary_key=True,
		default=generate_room_id
	)
	host_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
	
	host_user: Mapped["User"] = relationship(back_populates="rooms")
