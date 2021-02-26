"""add-unique-constraint

Revision ID: b387e3b7a15b
Revises: be1a23eb3fd7
Create Date: 2021-02-26 16:48:14.663752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b387e3b7a15b'
down_revision = 'be1a23eb3fd7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint('unq_name', 'participants', ["name", "board_id"])


def downgrade():
    op.drop_constraint('unq_name', 'participants')
