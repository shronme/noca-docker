"""Adding address1 column

Revision ID: 48c078bba015
Revises: 60695c537c21
Create Date: 2016-11-07 10:32:35.471105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48c078bba015'
down_revision = '60695c537c21'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('applicants', sa.Column('address_1', sa.String))


def downgrade():
    op.drop_column('applicants', 'address_1')
