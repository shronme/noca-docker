"""create applicants table

Revision ID: 06e8afe67022
Revises: 
Create Date: 2016-11-03 11:53:17.097775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06e8afe67022'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'applicants',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('applicants')
