"""Add auto_increment

Revision ID: 275183a3ab50
Revises: caf1dcc1f95b
Create Date: 2021-02-23 12:22:30.998075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '275183a3ab50'
down_revision = 'caf1dcc1f95b'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('score_boards', 'id' ,autoincrement=None)

def downgrade():
    pass
