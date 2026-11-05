import asyncio
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine

from alembic import context

from app.settings import Settings

settings = Settings()

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

config.set_main_option("sqlalchemy.url", settings.url_db)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
	fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

from app.infrastructure.database.base_model import Base

target_metadata = Base.metadata

if config.config_file_name is not None:
	fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata


def do_run_migration(connection):
	context.configure(
		compare_type=True,
		dialect_opts={"paramstyle": "named"},
		connection=connection,
		target_metadata=target_metadata,
	
	)
	
	with context.begin_transaction():
		context.run_migrations()


async def run_migrations_online() -> None:
	"""Run migrations in 'online' mode.

	In this scenario we need to create an Engine
	and associate a connection with the context.

	"""
	connectable = create_async_engine(settings.url_db, future=True)
	
	async with connectable.connect() as connection:
		await connection.run_sync(do_run_migration)


asyncio.run(run_migrations_online())
