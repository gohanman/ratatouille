# -*- coding: utf-8; mode: python -*-
"""
Rattail core data model extensions
"""

from __future__ import unicode_literals, absolute_import

import sqlalchemy as sa
from sqlalchemy import orm

from rattail.db import model
from rattail.db.core import uuid_column


class RatatouilleCustomer(model.Base):
    """
    Ratatouille extensions to core Customer model
    """
    __tablename__ = 'ratatouille_customer'
    __table_args__ = (
        sa.ForeignKeyConstraint(['uuid'], ['customer.uuid'], name='ratatouille_customer_fk_customer'),
    )

    uuid = uuid_column(default=None)

    customer = orm.relationship(
        model.Customer,
        doc="""
        Customer to which this extension record pertains.
        """,
        backref=orm.backref(
            '_ratatouille',
            uselist=False,
            cascade='all, delete-orphan',
            doc="""
            Ratatouille-specific extension record for the customer.
            """),
    )

    mail_list_synced = sa.Column(sa.Boolean(), nullable=False, default=False, doc="""
    Flag indicating whether the customer's email address has been synced to the
    general mailing list.
    """)

class Recipes(model.Base): 
    __tablename__ = 'recipes'

    uuid = uuid_column(default=None)

    store_id = sa.Column(sa.Integer(), nullable=True)
    recipe_id = sa.Column(sa.Integer(), nullable=True)

    name = sa.Column(sa.String(length=255), nullable=True)
    updated = sa.Column(sa.DateTime(), nullable=True)
    plu = sa.Column(sa.String(length=13), nullable=True)
    active = sa.Column(sa.Boolean(), nullable=False, default=False)

class RecipeItems(model.Base):
    __tablename__ = "recipe_items"

    uuid = uuid_column(default=None)

    store_id = sa.Column(sa.Integer(), nullable=True)
    item_id = sa.Column(sa.Integer(), nullable=True)

    name = sa.Column(sa.String(length=255), nullable=True)
    active = sa.Column(sa.Boolean(), nullable=False, default=False)

