# -*- coding: utf-8; mode: python; -*-
"""
Alembic environment script
"""

from __future__ import unicode_literals, absolute_import

from alembic import context
from sqlalchemy.orm import configure_mappers

from rattail.config import make_config
from rattail.db.util import get_default_engine
from rattail.db.continuum import configure_versioning


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
alembic_config = context.config

# use same config file for Rattail
rattail_config = make_config(alembic_config.config_file_name, usedb=False, versioning=False)

# configure Continuum..this is trickier than we want but it works..
configure_versioning(rattail_config, force=True)
from ratatouille.db import model
configure_mappers()

# needed for 'autogenerate' support
target_metadata = model.Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    engine = get_default_engine(rattail_config)
    context.configure(
        url=engine.url,
        target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    engine = get_default_engine(rattail_config)
    connection = engine.connect()
    context.configure(
        connection=connection,
        target_metadata=target_metadata)

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
