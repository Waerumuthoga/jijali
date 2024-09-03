"""create moods table

Revision ID: cbece4e82bf6
Revises: edfb6c5d85f0
Create Date: 2024-09-03 00:48:37.013359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbece4e82bf6'
down_revision: Union[str, None] = 'edfb6c5d85f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('moods',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=True),
                    sa.Column('content', sa.String(), nullable=False),
                    sa.Column('status', sa.Boolean(), nullable=False, server_default='FALSE'),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))
                    )
    pass


def downgrade() -> None:
    op.drop_table('moods')
    pass
