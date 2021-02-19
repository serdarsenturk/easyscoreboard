"""create scoreboard table

Revision ID: caf1dcc1f95b
Revises: 
Create Date: 2021-02-19 11:12:44.347582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caf1dcc1f95b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'scoreboard',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(25), nullable=False)
    )


def downgrade():
    op.drop_table('scoreboard')
    
