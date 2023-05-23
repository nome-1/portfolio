"""create Post table

Revision ID: 37325a321161
Revises: 
Create Date: 2023-04-11 17:30:05.493045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37325a321161'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Post',sa.Column('id',sa.Integer(),nullable=False,primary_key=True)
                    ,sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('Post')
    pass
