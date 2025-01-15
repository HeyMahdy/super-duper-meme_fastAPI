import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from models.base import Model1Base as Base
from dotenv import load_dotenv

load_dotenv()
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
# Access the Alembic Config object to get values from alembic.ini
config = context.config

# Log file configuration, if necessary
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set metadata for autogeneration (use SQLAlchemy Base)
target_metadata = Base.metadata

# Set SQLAlchemy URL dynamically using the environment variable
config.set_main_option('sqlalchemy.url', os.getenv("DATABASE_URL"))


# ---------------------------------------------------------
# Migration Functions:
# ---------------------------------------------------------
def run_migrations_offline():
    """Run migrations in 'offline' mode without a DB connection."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode with a DB connection."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


# ---------------------------------------------------------
# Check Mode and Run:
# ---------------------------------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
