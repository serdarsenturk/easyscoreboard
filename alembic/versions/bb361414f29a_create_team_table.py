"""create team table

Revision ID: bb361414f29a
Revises: 21c7ee6c7a4d
Create Date: 2021-02-24 13:42:09.191078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb361414f29a'
down_revision = '21c7ee6c7a4d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'team',
        sa.Column('table_id', sa.Integer(), primary_key=True),
        sa.Column('table_name', sa.VARCHAR(25), nullable=False),
        sa.Column('prts_id', sa.Integer(), nullable=False),
        sa.Column('member_num', sa.Integer(), nullable=False),
        sa.Column('member_cap', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('table_id')
    )


def downgrade():
    op.drop_table('team')
