"""create participant table

Revision ID: 21c7ee6c7a4d
Revises: caf1dcc1f95b
Create Date: 2021-02-24 13:15:53.327813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21c7ee6c7a4d'
down_revision = 'caf1dcc1f95b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'participant',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.VARCHAR(25), nullable=False),
        sa.Column('board_id', sa.Integer(), nullable=False),
        sa.Column('score', sa.Integer(), server_default='0')
    )


def downgrade():
    op.drop_table('participant')
