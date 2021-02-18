"""create account table

Revision ID: 8a3b9e9f40e5
Revises: 
Create Date: 2021-02-18 15:28:41.416787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a3b9e9f40e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'scores',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('score', sa.Integer, nullable=False),
        sa.Column('description', sa.Unicode(200))
    )


def downgrade():
    op.drop_table('scores)
