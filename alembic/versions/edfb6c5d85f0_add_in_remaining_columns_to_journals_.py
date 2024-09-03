"""add in remaining columns to journals table

Revision ID: edfb6c5d85f0
Revises: 9331ff6695d2
Create Date: 2024-09-03 00:33:47.312153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edfb6c5d85f0'
down_revision: Union[str, None] = '9331ff6695d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('journals', sa.Column('status', sa.Boolean(), nullable=False, server_default='FALSE'))
    op.add_column('journals', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),)
    pass


def downgrade() -> None:
    op.drop_column('journals', 'status')
    op.drop_column('journals', 'created_at')
    pass
