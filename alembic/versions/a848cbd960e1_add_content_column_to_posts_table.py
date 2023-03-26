"""add_content_column_to_posts_table

Revision ID: a848cbd960e1
Revises: 6acfdd11a120
Create Date: 2023-03-24 00:51:23.905023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a848cbd960e1'
down_revision = '6acfdd11a120'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
