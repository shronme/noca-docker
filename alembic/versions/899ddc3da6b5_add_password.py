"""add password

Revision ID: 899ddc3da6b5
Revises: 06e8afe67022
Create Date: 2016-11-03 15:03:47.501134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '899ddc3da6b5'
down_revision = '06e8afe67022'
branch_labels = None
depends_on = None

def upgrade():
    sa.Column('password', sa.String(50), nullable=False)


def downgrade():
    pass
