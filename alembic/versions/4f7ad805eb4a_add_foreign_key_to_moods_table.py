"""add foreign_key to moods table

Revision ID: 4f7ad805eb4a
Revises: cbece4e82bf6
Create Date: 2024-09-03 00:57:22.135163

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f7ad805eb4a'
down_revision: Union[str, None] = 'cbece4e82bf6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('moods', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('moods_users_fk', source_table="moods", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('moods_users_fk', table_name="moods")
    op.drop_column('moods', 'owner_id')
    pass
