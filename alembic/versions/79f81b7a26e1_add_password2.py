"""add password2

Revision ID: 79f81b7a26e1
Revises: 899ddc3da6b5
Create Date: 2016-11-03 15:09:14.225781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79f81b7a26e1'
down_revision = '899ddc3da6b5'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('applicants', sa.Column('password', sa.String))


def downgrade():
    pass
