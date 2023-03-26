"""add foreign-key to posts table

Revision ID: 4f27363e610a
Revises: 2c6a6cf07402
Create Date: 2023-03-24 05:00:07.501637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f27363e610a'
down_revision = '2c6a6cf07402'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                           local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
