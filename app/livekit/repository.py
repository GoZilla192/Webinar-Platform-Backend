from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

from app.livekit.models import Room

class LiveKitRepository:
	"Work with ORM model Room"
	def __init__(self, db_session: AsyncSession):
		"""Initialize the repository with a database session."""
		self.db_session = db_session
		
	async def create_room(self, user_id: int) -> str:
		"""Create room"""
		room = Room(host_user_id=user_id)
		
		self.db_session.add(room)
		
		try:
			await self.db_session.flush()
			await self.db_session.commit()
		except IntegrityError:
			raise UserAlreadyExists
		
		return room.room_id
	
	async def is_room_exist(self, room_id: str) -> bool:
		"""Check if room exist"""
		res = await self.db_session.execute(
			select(Room).where(Room.room_id == room_id)
		)
		
		return bool(res.scalar_one_or_none())
