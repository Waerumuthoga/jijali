"""add foreign_key to journals table

Revision ID: 9331ff6695d2
Revises: ab8c1a41ea3f
Create Date: 2024-09-03 00:19:10.597027

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9331ff6695d2'
down_revision: Union[str, None] = 'ab8c1a41ea3f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('journals', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('journals_users_fk', source_table="journals", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('journals_users_fk', table_name="journals")
    op.drop_column('journals', 'owner_id')
    pass
