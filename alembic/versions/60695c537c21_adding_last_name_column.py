"""Adding last name column

Revision ID: 60695c537c21
Revises: 79f81b7a26e1
Create Date: 2016-11-07 09:46:37.112079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60695c537c21'
down_revision = '79f81b7a26e1'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('applicants', sa.Column('last_name', sa.String))


def downgrade():
    op.drop_column('applicants', 'last_name')
