"""Renaming students to scholars

Revision ID: d67975ad9b0d
Revises: 791279dd0760
Create Date: 2023-06-01 14:40:37.604090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd67975ad9b0d'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')

    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')

    pass
