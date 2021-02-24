"""add constraint

Revision ID: be1a23eb3fd7
Revises: 21c7ee6c7a4d
Create Date: 2021-02-24 15:19:00.256754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be1a23eb3fd7'
down_revision = '21c7ee6c7a4d'
branch_labels = None
depends_on = None



def upgrade():
    op.create_foreign_key(
        "fk_participant_key",
        "score_boards",
        "participant",
        ["participant"],
        ["prt_id"]
    )


def downgrade():
    pass
