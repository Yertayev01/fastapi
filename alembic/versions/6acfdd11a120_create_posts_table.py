"""create posts table

Revision ID: 6acfdd11a120
Revises: 
Create Date: 2023-03-24 00:13:10.808237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6acfdd11a120'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(),  nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
